from django.shortcuts import render

from django.http import HttpResponse
from to_do.models import Question
from django.contrib.auth.decorators import login_required


def index(request):
    #return HttpResponse('olá django - index')
    #return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'ultima enquete '})



@login_required
def ola(request):
    #return HttpResponse('olá django')
    questions = Question.objects.all()
    context = {' all_questions ': questions }
    return render(request, 'Polls/questions.html', context) 