from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)
    answer_selected = models.BooleanField(default="False")

    def __str__(self):
        return self.question


class Scores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.CharField(max_length = 200)
