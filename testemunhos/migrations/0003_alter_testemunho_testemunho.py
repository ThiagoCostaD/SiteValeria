# Generated by Django 4.2.2 on 2023-07-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testemunhos', '0002_rename_testemunhos_testemunho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testemunho',
            name='testemunho',
            field=models.TextField(),
        ),
    ]