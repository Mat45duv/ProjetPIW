from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_films, name='accueil'),
    path('films/', views.liste_films, name='films'),
    path('film/<int:film_id>/', views.representations_film, name='film_reps'),
    path('representation/<int:id>/', views.detail_representation, name='detail'),
    path('reserver/<int:id>/', views.reserver, name='reserver'),
    path('confirmation/', views.confirmation, name='confirmation'),


    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),

    # FILMS
    path('admin-panel/films/', views.admin_films, name='admin_films'),
    path('admin-panel/films/add/', views.admin_add_film, name='admin_add_film'),
    path('admin-panel/films/edit/<int:id>/', views.admin_edit_film, name='admin_edit_film'),
    path('admin-panel/films/delete/<int:id>/', views.admin_delete_film, name='admin_delete_film'),

    # SALLES
    path('admin-panel/salles/', views.admin_salles, name='admin_salles'),

    # REPRESENTATIONS
    path('admin-panel/representations/', views.admin_reps, name='admin_reps'),
]
