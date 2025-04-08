from django.shortcuts import get_object_or_404, redirect, render
from base.views import BaseListView, BaseView, BaseCreateView
from qna.models import Question, Like, Answer
from django.http import JsonResponse
from qna.forms import QuestionCreateForm, AnswerCreateForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.shortcuts import HttpResponse, HttpResponseRedirect

# Create your views here.

class HomeView(BaseListView):
    model = Question
    template_name = "qna/home.html"
    context_object_name = "questions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all().order_by('-created_at')
        user_liked_answers = Like.objects.filter(user=self.request.user).values_list('answer_id', flat=True)
        context['liked_answers'] = set(user_liked_answers)
        return context


class ToggleLike(BaseView):
    def post(self, request, *args, **kwargs):
        answer_id = request.POST.get("answer_id")
        answer = get_object_or_404(Answer, id=answer_id)

        like, created = Like.objects.get_or_create(user=request.user, answer=answer)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        like_count = Like.objects.filter(answer=answer).count()
        return JsonResponse({"liked": liked, "like_count": like_count})

class CreateQuestion(BaseCreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = "qna/create_question.html"
    success_url = reverse_lazy("qna:my_question")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        messages.success(self.request, "Question Created Successfully.")
        return HttpResponseRedirect(reverse("qna:my_question"))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
class MyQuestionsView(BaseListView):
    model = Question
    template_name = "qna/my_questions.html"
    context_object_name = "questions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(user=self.request.user).order_by('-created_at')
        user_liked_answers = Like.objects.filter(user=self.request.user).values_list('answer_id', flat=True)
        context['liked_answers'] = set(user_liked_answers)
        return context
    
class AnswerCreateView(BaseView):
    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        form = AnswerCreateForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
        return redirect("qna:home")

class UpdateQuestionView(BaseView):
    def post(self, request):
        question_id = request.POST.get('question_id')
        question = request.POST.get('question')

        try:
            question_obj = Question.objects.get(id=question_id, user=request.user)
            question_obj.question = question
            question_obj.save()
            return JsonResponse({'status': 'success'})
        except Question.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Question not found'}, status=404)
        
class DeleteQuestionView(BaseView):
    def post(self, request):
        question_id = request.POST.get('question_id')
        try:
            question = Question.objects.get(id=question_id, user=request.user)
            question.delete()
            return JsonResponse({'status': 'success'})
        except Question.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Question not found'}, status=404)