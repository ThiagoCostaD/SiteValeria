# Generated by Django 4.2.2 on 2023-07-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testemunhos', '0004_alter_testemunho_options_alter_categoria_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testemunho',
            name='slug',
            field=models.SlugField(help_text='Slug do testemunho'),
        ),
    ]