from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser, BaseModel):
    phone = models.CharField(_("Phone"), max_length=20, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=255, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"