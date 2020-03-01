from django.db import models
from django import forms


class Project(models.Model):
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    desctiption = models.CharField(max_length=100)
    photo = models.CharField(max_length=256)
