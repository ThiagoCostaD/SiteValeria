from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)


class Testemunhos(models.Model):

    titulo = models.CharField(max_length=77)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField()
    testemunho = models.TimeField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='testemunhos/img/%Y/%m/%d/')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True
    )
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
