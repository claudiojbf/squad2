# Generated by Django 4.1 on 2022-09-08 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_atleta', '0002_alter_atletas_naturalidade_uf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atletas',
            name='idade',
        ),
    ]
