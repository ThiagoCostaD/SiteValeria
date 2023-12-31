# Generated by Django 4.2.2 on 2023-07-07 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testemunhos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=77)),
                ('descricao', models.CharField(max_length=165)),
                ('slug', models.SlugField()),
                ('testemunho', models.TimeField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
                ('publicado', models.BooleanField(default=False)),
                ('foto', models.ImageField(upload_to='testemunhos/img/%Y/%m/%d/')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testemunhos.categoria')),
            ],
        ),
    ]
