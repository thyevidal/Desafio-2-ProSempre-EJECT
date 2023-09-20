from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user_imagem = models.ImageField(null=True, blank=True, upload_to='usuario')
    u_apelido = models.TextField(null=True, blank=True, max_length=126)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
