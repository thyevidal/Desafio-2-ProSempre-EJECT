from django.db import models
from datetime import datetime

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)
    imagem = models.ImageField(upload_to='fotos/%d/%m/%y')
    descricao = models.TextField(max_length=510, null=True, blank=True)
    categoria = models.TextField(max_length=61, null=True, blank=True)
    tempo = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nome

