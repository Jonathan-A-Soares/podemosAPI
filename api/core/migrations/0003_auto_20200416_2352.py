# Generated by Django 3.0.4 on 2020-04-17 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aluno_conteudos_cursos_noticias'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
