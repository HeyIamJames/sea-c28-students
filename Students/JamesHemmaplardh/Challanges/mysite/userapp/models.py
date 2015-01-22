from django.db import models
from django.core import validators


class User(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)


# Create your models here.
