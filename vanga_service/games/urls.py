from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.gamesList),
    path('createGame/', views.createGame)
]