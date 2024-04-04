"""
Importa a classe `AppConfig` do Django para configuração de aplicativos.
"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Classe de configuração para a aplicação 'accounts'."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
