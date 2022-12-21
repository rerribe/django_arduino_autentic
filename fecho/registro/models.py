from django.db import models
#from django.contrib.auth.models import User
# Create your models here.


# def cartao_default():
#     return {"chave":"111,222,333,444"}
#     # return dict(valor)

class Registro(models.Model):
	nome = models.CharField(default='',max_length=200)
	cargo = models.CharField(default='',max_length=200)
	cartao = models.CharField(default='',max_length=200)


