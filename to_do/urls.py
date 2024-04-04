""" Caminho das URLS """
from django.urls import path
from to_do.views import index, ola, QuestionCreateView, QuestionUpdateView
from to_do.views import QuestionDeleteView
from to_do import views

urlpatterns = [
    path('index/', index, name="index"),
    path('ola/', ola, name="ola"),
    path('enquete/add', QuestionCreateView.as_view(), name="poll_add"),
    path('enquete/<int:pk>/edit', QuestionUpdateView.as_view(),
         name="question_edit"),
    path('enquete/<int:pk>', QuestionDeleteView.as_view(),
         name="question_delete"),
    path('enquete/<int:pk>/show', views.QuestionDetailView.as_view(),
         name="question_detail"),
    path('enquete/list',
         views.QuestionListView.as_view(), name="polls_list"),
    path('about-us',
         views.SobreTemplateView.as_view(),
         name="about_page"),
]
