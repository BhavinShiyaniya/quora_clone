from django import forms
from qna.models import Question, Answer

class QuestionCreateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ["question"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = ""

        self.fields["question"].required = True

class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']