from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.edit  import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib  import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
User = get_user_model()

from accounts.forms import AccountSignupForm

class AccountCreatView(CreateView):
    model = User
    template_name = 'registration/signup_form.html'
    form_class  = AccountSignupForm
    success_url = reverse_lazy('login')
    message = 'Usuário criado com sucesso.'

    def form_valid(self, form) -> HttpResponse:
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.message)

        return super(AccountCreatView, self).form_valid(form)
    

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name  = 'accounts/user_form.html'
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
    
