# Generated by Django 4.2.5 on 2023-09-14 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.IntegerField(max_length=8)),
                ('foto', models.FileField(upload_to='')),
            ],
        ),
    ]