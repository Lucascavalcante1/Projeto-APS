""" Caminho das URLS """
from django.urls import path, include
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
    path('enquete/<int:question_id>/vote',
         views.vote,
         name="poll_vote"
         ),
    path('enquete/<int:question_id>/results',
         views.results,
         name = "poll_result"
    ),
     path('enquete/<int:pk>/alternativa/add',
         views.ChoiceCreateView.as_view(),
         name = "choice_add"
    ),
     path('enquete/<int:pk>/alternativa/edit',
         views.ChoiceUpdateView.as_view(),
         name = "choice_edit"
    ),
     path('enquete/<int:pk>/alternativa/delete',
         views.ChoiceDeleteView.as_view(),
         name = "choice_delete"
    ),

]
