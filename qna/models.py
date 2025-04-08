from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.

class Question(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(_("Question"))

    def __Str__(self):
        return f"{self.question}"

class Answer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(_("Answer"))

    def __str__(self):
        return f"{self.answer}"

class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['answer', 'user']