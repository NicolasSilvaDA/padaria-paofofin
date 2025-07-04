# Generated by Django 5.2.1 on 2025-06-01 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Padaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('login_padaria', models.TextField()),
                ('senha_padaria', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('data_nasc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('tempo_preparo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Padaria_produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('padaria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.padaria')),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_usuario', models.TextField()),
                ('senha_usuario', models.TextField()),
                ('pessoa_cpf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao_usuario_padaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('padaria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.padaria')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.usuario')),
            ],
        ),
    ]
