from django.urls import path
from qna.views import HomeView, ToggleLike, CreateQuestion, MyQuestionsView, AnswerCreateView, UpdateQuestionView, DeleteQuestionView

app_name = "qna"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('toggle-like/', ToggleLike.as_view(), name='toggle_like'),
    path('create-question/', CreateQuestion.as_view(), name='create_question'),
    path('my-question/', MyQuestionsView.as_view(), name='my_question'),
    path('answer/create/<int:pk>/', AnswerCreateView.as_view(), name='answer_create'),
    path('update-question/', UpdateQuestionView.as_view(), name='update_question'),
    path('delete-question/', DeleteQuestionView.as_view(), name='delete_question'),
]
