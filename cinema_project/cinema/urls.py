from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('films/', views.films, name='films'),
    path('a-propos/', views.a_propos, name='a_propos'),
    path('documentation/', views.documentation, name='documentation'),
]
