# Generated by Django 5.1.2 on 2024-11-12 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_usuario_delete_leitor_autor_cpf_autor_data_nasc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='data_nasc',
            field=models.DateField(default='2000-01-01', verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='razao_social',
            field=models.CharField(default='', verbose_name='Razão Social'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_nasc',
            field=models.DateField(default='2000-01-01', verbose_name='Data de Nascimento'),
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emp', models.DateField(verbose_name='Data de Emprestimo')),
                ('livro_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro', verbose_name='livro emprestado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario que pegou o livro')),
            ],
            options={
                'verbose_name': 'Emprestimo',
                'verbose_name_plural': 'Emprestimos',
            },
        ),
    ]
