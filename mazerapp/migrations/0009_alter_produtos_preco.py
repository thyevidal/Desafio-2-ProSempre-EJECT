# Generated by Django 4.2.5 on 2023-09-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mazerapp', '0008_rename_produto_produtos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='preco',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
