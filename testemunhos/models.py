from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(
        max_length=50, help_text='Nome da categoria')

    def __str__(self):
        return self.nome


class Testemunho(models.Model):

    titulo = models.CharField(
        max_length=77, help_text='Título do testemunho', blank=False)
    descricao = models.CharField(
        max_length=165, help_text='Descrição do testemunho', blank=False)
    slug = models.SlugField(
        help_text='Slug do testemunho', blank=False, unique=True)
    testemunho = models.TextField(help_text='Texto do testemunho', blank=False)
    data_criacao = models.DateTimeField(
        auto_now_add=True, help_text='Data de criação do testemunho')
    data_modificacao = models.DateTimeField(
        auto_now=True, help_text='Data de modificação do testemunho')
    publicado = models.BooleanField(
        default=False,
        help_text='Indica se o testemunho está publicado ou não')
    foto = models.ImageField(
        upload_to='testemunhos/img/%Y/%m/%d/', help_text='Foto do testemunho')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True,
        blank=True, default=None, help_text='Categoria do testemunho',
        related_name='testemunhos', related_query_name='testemunho_categoria'
    )
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        blank=True, default=None, help_text='Autor do testemunho',
        related_name='testemunhos', related_query_name='testemunho_autor'
    )

    class Meta:
        verbose_name = 'Testemunho'
        verbose_name_plural = 'Testemunhos'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo
