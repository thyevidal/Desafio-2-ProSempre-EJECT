# Generated by Django 4.2.5 on 2023-09-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mazerapp', '0005_alter_produto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.TextField(max_length=255),
        ),
    ]
