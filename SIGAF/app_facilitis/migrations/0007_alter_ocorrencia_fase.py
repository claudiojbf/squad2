# Generated by Django 4.1 on 2022-09-27 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_facilitis', '0006_remove_ocorrencia_status_ocorrencia_fase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='fase',
            field=models.CharField(default='P', max_length=2),
        ),
    ]
