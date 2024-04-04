"""
Importa os módulos necessários do Django para criar visualizações genéricas,
lidar com URLs, fazer hash de senhas, exibir mensagens, lidar com autenticação,
e obter o modelo de usuário atual.
"""
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from accounts.forms import AccountSignupForm
User = get_user_model()


class AccountCreatView(CreateView):
    """""
    Esta view renderiza um formulário de registro de usuário e permite ao
    usuário  criar uma nova conta.
    Após a criação bem-sucedida da conta, redireciona para a página de login.
    """""
    model = User
    template_name = 'registration/signup_form.html'
    form_class = AccountSignupForm
    success_url = reverse_lazy('login')
    message = 'Usuário criado com sucesso.'

    def form_valid(self, form) -> HttpResponse:
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.message)

        return super(AccountCreatView, self).form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """""
    Este método é chamado quando o formulário de registro é válido.
    Ele hash a senha do usuário, salva o novo usuário e
    exibe uma mensagem de sucesso.
    """""

    model = User
    template_name = 'accounts/user_form.html'
    fields = ('first_name', 'email', 'imagem', )
    success_url = reverse_lazy('index')
    success_message = 'Perfil Atualizado Com Sucesso'

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        user = self.request.user
        if user is None or not user.is_authenticated or user_id != user_id:
            return User.objects.none()
        return User.objects.filter(id=user.id)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
