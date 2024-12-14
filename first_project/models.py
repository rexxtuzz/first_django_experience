from django.db import models


class ExpressionHistory(models.Model):
    expression = models.CharField(max_length=100)
    answer = models.IntegerField()
