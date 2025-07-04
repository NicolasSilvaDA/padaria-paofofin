# Generated by Django 5.2.1 on 2025-06-01 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_padaria_login_padaria_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Pessoa_usuario',
        ),
        migrations.AlterField(
            model_name='inscricao_usuario_padaria',
            name='padaria_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.padaria_usuario'),
        ),
        migrations.AlterField(
            model_name='padaria_produtos',
            name='padaria_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.padaria_usuario'),
        ),
    ]
