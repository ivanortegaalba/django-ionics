# coding: utf8

from django.db import models

# Create your models here.
class Question(models.Model):
    questionTest = models.CharField(max_length=200) #Sera la longitud del varchar en la bd
    pubDate = models.DateTimeField('Date published')

    def __str__(self):
        return self.questionTest

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText
