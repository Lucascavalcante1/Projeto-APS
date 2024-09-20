"""""
Importa os módulos necessários do Django para definir modelos de banco de dados
e um modelo de usuário personalizado.
"""""
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    """Este modelo estende o modelo `AbstractUser` fornecido pelo Django,
    adicionando campos personalizados para data de nascimento, CPF e imagem
    de perfil do usuário.
    """
    data_nascimento = models.DateField(
        "Data De Nascimento",
        null=True,
        blank=True
    )
    cpf = models.CharField(
        "CPF",
        max_length=11,
        null=True,
        blank=True
    )
    imagem = models.FileField(
        upload_to='image/user',
        default=None,
        null=True,
        blank=True,
    )
