from django.db import models
from django.contrib.auth.models import User


class ExpressionHistory(models.Model):
    expression = models.CharField(max_length=100)
    answer = models.IntegerField()


class StrHistory(models.Model):
    str = models.CharField(max_length=100)
    words_count = models.IntegerField()
    nums_count = models.IntegerField()
    time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
