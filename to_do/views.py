from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib import messages
from to_do.models import Question, Choice
from to_do.forms import QuestionForm    
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
    """ Create"""
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
    """ Delete """
    model = Question
    template_name = 'Polls/question_confirm_delete_form.html'
    success_url = reverse_lazy('index')
    success_message = 'A pergunta foi excluida com sucesso'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(QuestionDeleteView, self).form_valid(form)


class QuestionDetailView(DetailView):
    """ View """
    model = Question
    template_name = 'Polls/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        question = kwargs.get('object')
        context['total_votes'] = question.get_total_votes
        return context


class QuestionListView(ListView):
    """ Listar """
    model = Question
    template_name = 'Polls/question_list.html'
    context_object_name = 'questions'


class SobreTemplateView(TemplateView):
    """ Template do Sobre """
    template_name = 'Polls/sobre.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            messages.error(request, 'Selecione uma alternativa para votar')
        else:
            selected_choice.votes += 1
            selected_choice.save()
            messages.success(request, 'Seu voto foi registrado com sucesso')
            return redirect(reverse_lazy("poll_vote", args=(question.id,)))
    
    context = {'question': question}
    return redirect(reverse_lazy("poll_result", args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    votes = Choice.objects.filter(question=question).aggregate(total=Sum('votes')) or 0
    total_votes = votes.get('total')
    context = {'question': question}
    context['votes'] = []
    for choice in question.choice_set.all():
        percentage = 0
        if choice.votes > 0 and total_votes > 0:
            percentage = choice.votes / total_votes * 100

        context['votes'].append(
            {
                'text': choice.choice_text,
                'votes': choice.votes,
                'percentage': round(percentage, 2)
            }
        )
    return render(request, "polls/results.html", context)

class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'Polls/choice_form.html'
    fields = ('choice_text', )
    success_message = 'Pergunta criada com sucesso!'

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        return super(ChoiceCreateView, self).dispatch(request,  *args, **kwargs)

    def get_context_data(self, **kwargs):
        # question = get_object_or_404(Question,  pk=self.kwargs.get('pk'))
        context = super(ChoiceCreateView, self).get_context_data(**kwargs)
        context['form_title'] = f'Alternativa para:{self.question.question_text}'

        return context

    def form_valid(self, form):
        form.instance.question = self.question
        messages.success(self.request, self.success_message)
        return super(ChoiceCreateView, self).form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        question_id = self.kwargs.get('pk')
        return reverse_lazy('question_edit', kwargs={'pk': question_id})

class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'polls/choice_form.html'
    fields = ('choice_text', )
    success_message = 'Alternativa atualizada com sucesso!'

    def get_context_data(self, **kwargs):
        context = super(ChoiceUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Editando alternativa'
        return context
    
    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ChoiceUpdateView, self).form_valid(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        question_id = self.object.question.id
        return reverse_lazy('question_edit', kwargs={'pk': question_id})

class ChoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Choice
    template_name = 'polls/choice_confirm_delete_form.html'
    success_message = 'Alternativa excluída com sucesso!'

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ChoiceDeleteView, self).form_valid(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        question_id = self.object.question.id
        print(question_id)
        return reverse_lazy('question_edit', kwargs={'pk': question_id})