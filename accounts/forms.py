"""""
Importa os módulos necessários do Django para trabalhar com formulários e
gerenciamento de autenticação de usuário.
"""""
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountSignupForm(forms.ModelForm):
    """""
    Um formulário para registro de contas de usuário.
    Este formulário é utilizado para criar novas contas de usuário no sistema.
    Ele inclui campos para
    o nome de usuário, email, data de nascimento, CPF e senha.
    """""
    password = forms.CharField(
        label="Senha",
        max_length=100,
        widget=forms.PasswordInput()
    )

    class Meta:
        """Esta metaclasse fornece informações adicionais sobre o formulário,
        incluindo o modelo associado e os campos que devem ser
        incluídos no formulário."""
        model = User
        fields = ('username', 'email', 'data_nascimento', 'cpf', 'password')
        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date', 'required': 'required'}
            )
        }
