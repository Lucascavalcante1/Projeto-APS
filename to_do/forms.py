from django import forms 
from to_do.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')
        widgets = {
            'pub_date': forms.DateInput(format='%Y-%m-%d'),
        }