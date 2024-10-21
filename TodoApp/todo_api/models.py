from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

import enum
from django.utils.translation import gettext_lazy as _



# Create your models here.


# class TodoType(enum.Enum):
#     High = 'High'
#     Low = 'Low'

class Todo(models.Model):

    class TodoType(models.TextChoices):
        HIGH = 'H',_('High')
        LOW = 'L',_('Low')
        NULL = 'N',_('None')

    task = models.CharField(max_length=100)
    priority = models.CharField(max_length=4 ,choices=TodoType.choices, default=TodoType.NULL)
    # priority = models.CharField(choices=[(TodoType.High, 'High'),(TodoType.Low, 'Low')])
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    is_completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    def __str__(self) -> str:
        return self.task



