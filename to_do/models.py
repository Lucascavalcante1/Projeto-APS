from django.db import models

class Question(models.Model):
    question_text = models.CharField("Pergunta", max_length=300)
    pub_date = models.DateField("Data de publicação")

    class Meta: 
        verbose_name_plural = 'Perguntas'
        verbose_name = 'Pergunta'
        
