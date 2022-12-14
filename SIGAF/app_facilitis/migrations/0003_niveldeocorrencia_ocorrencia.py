# Generated by Django 4.1 on 2022-09-01 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_facilitis', '0002_rename_cadastro_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelDeOcorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=1)),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhes_ocorrencia', models.TextField()),
                ('descricao_ocorrido', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facilitis.local')),
                ('nivel_urgencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facilitis.niveldeocorrencia')),
            ],
        ),
    ]
