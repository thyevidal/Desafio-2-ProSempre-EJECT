# Generated by Django 4.2.5 on 2023-09-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mazerapp', '0004_alter_produto_imagem_alter_usuario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.TextField(default='nome', max_length=255),
        ),
    ]
