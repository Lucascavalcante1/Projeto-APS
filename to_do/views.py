from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib import messages
from to_do.models import Question
from to_do.forms import QuestionForm


def index(request):
    """Index"""
    aviso = 'Página Ainda Em Desenvolvimento'
    messages.warning(request, aviso)
    questions = Question.objects.all()
    context = {'all_questions': questions, 'titulo': 'Ultimas Enquetes '}
    return render(request, 'Polls/questions.html', context)


@login_required


def ola(request):
    """Pagina Home"""
    questions = Question.objects.all()
    context = {'all_questions': questions}
    return render(request, 'Polls/questions.html', context)


class QuestionCreateView(LoginRequiredMixin, CreateView):
    """ Criar """
    model = Question
    template_name = 'Polls/question_form.html'
    fields = ('question_text', 'pub_date')
    success_url = reverse_lazy('index')
    success_message = 'Pergunta Criada Com Sucesso.'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(QuestionCreateView, self).form_valid(form)   

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Criando Uma Pergunta'

        return context


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    """ Update """
    model = Question
    template_name = 'polls/question_form.html'
    success_url = reverse_lazy('index')
    form_class = QuestionForm
    success_message = 'Pergunta Atualizada com sucesso'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Editando a Pergunta'

        return context


class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    """ Deletar """
    model = Question
    template_name = 'Polls/question_confirm_delete_form.html'
    success_url = reverse_lazy('index')
    success_message = 'A pergunta foi excluida com sucesso'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(QuestionDeleteView, self).form_valid(form)


class QuestionDetailView(DetailView):
    """ Ver """
    model = Question
    template_name = 'Polls/question_detail.html'
    context_object_name = 'question'


class QuestionListView(ListView):
    """ Listar """
    model = Question
    template_name = 'Polls/question_list.html'
    context_object_name = 'questions'


class SobreTemplateView(TemplateView):
    """ Template do Sobre """
    template_name = 'Polls/sobre.html'
