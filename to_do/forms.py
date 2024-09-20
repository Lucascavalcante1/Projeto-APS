"""""
"""""
from django import forms
from to_do.models import Question


class QuestionForm(forms.ModelForm):
    """Formulário para adicionar uma nova pergunta."""
    class Meta:
        """""
        Metaclasse para o formulário de pergunta.
        """""
        model = Question
        fields = ('question_text', 'pub_date')
        widgets = {
            'pub_date': forms.DateInput(format='%Y-%m-%d'),
        }
