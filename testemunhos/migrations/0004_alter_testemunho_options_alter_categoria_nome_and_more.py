# Generated by Django 4.2.2 on 2023-07-15 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testemunhos', '0003_alter_testemunho_testemunho'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testemunho',
            options={'ordering': ['-data_criacao'], 'verbose_name': 'Testemunho', 'verbose_name_plural': 'Testemunhos'},
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(help_text='Nome da categoria', max_length=50),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='autor',
            field=models.ForeignKey(blank=True, default=None, help_text='Autor do testemunho', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testemunhos', related_query_name='testemunho_autor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='categoria',
            field=models.ForeignKey(blank=True, default=None, help_text='Categoria do testemunho', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testemunhos', related_query_name='testemunho_categoria', to='testemunhos.categoria'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, help_text='Data de criação do testemunho'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='data_modificacao',
            field=models.DateTimeField(auto_now=True, help_text='Data de modificação do testemunho'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='descricao',
            field=models.CharField(help_text='Descrição do testemunho', max_length=165),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='foto',
            field=models.ImageField(help_text='Foto do testemunho', upload_to='testemunhos/img/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='publicado',
            field=models.BooleanField(default=False, help_text='Indica se o testemunho está publicado ou não'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='slug',
            field=models.SlugField(help_text='Slug do testemunho', unique=True),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='testemunho',
            field=models.TextField(help_text='Texto do testemunho'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='titulo',
            field=models.CharField(help_text='Título do testemunho', max_length=77),
        ),
    ]
