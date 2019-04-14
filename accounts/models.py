from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poll(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateField()

    def __str__(self):
        return self.text


class UserPolls(models.Model):
    #this is a user poll, this will create a poll for the user which is currently logged in, the score will be calculated based on the choices the user makes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, blank=True, null=True)


class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.choice_text[:25])

#choice model, one question has multiple choices, do not have to hardcode anything
class Question(models.Model):
    question_text = models.CharField(max_length=400)
    choices  = models.ManyToManyField(Choice, blank=True, null=True, related_name='choices')

    def __str__(self):
        return self.question_text


class Advice(models.Model):
    advice_text = models.CharField(max_length=500)
    min_score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    def __str__(self):
        return self.advice_text
# Question: are you employed:

# Choices:
# I am employed
# 50

# I am not employed
# 25
