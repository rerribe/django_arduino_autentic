from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Registro(models.Model):
	nome = models.CharField(max_length=200)
	cargo = models.CharField(max_length=200)
	cartao = models.CharField(max_length=200, default='default')