from django.urls import path, include
from board import views

urlpatterns = [
    path('', views.board),
    path('fisrt/', views.boardfirst),
    
]