# Generated by Django 4.2.2 on 2023-07-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testemunhos', '0005_alter_testemunho_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testemunho',
            name='slug',
            field=models.SlugField(help_text='Slug do testemunho', unique=True),
        ),
    ]
