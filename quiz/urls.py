from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start_round, name='start_round'),
    path('round/', views.quiz_round, name='quiz_round'),
    path('round/next/', views.quiz_round_next, name='quiz_round_next'),
    path('duel/', views.start_duel, name='start_duel'),
    path('duel/play/', views.duel_play, name='duel_play'),
]
