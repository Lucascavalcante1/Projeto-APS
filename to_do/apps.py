"""
Importa a classe `AppConfig` do Django para configuração de aplicativos.
"""
from django.apps import AppConfig


class ToDoConfig(AppConfig):
    """Configuração da aplicação 'to_do'."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'to_do'
    verbose_name = 'Enquetes'
