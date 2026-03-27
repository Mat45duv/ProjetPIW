from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.accueil, name='accueil'),
    path('films/', views.liste_films, name='films'),
    path('film/<int:film_id>/', views.representations_film, name='film_reps'),
    path('representation/<int:id>/', views.detail_representation, name='detail'),
    path('reserver/<int:id>/', views.reserver, name='reserver'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('a-propos/', views.a_propos, name='a_propos'),

  
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),

   
    path('admin-panel/films/', views.admin_films, name='admin_films'),
    path('admin-panel/films/add/', views.admin_add_film, name='admin_add_film'),
    path('admin-panel/films/edit/<int:id>/', views.admin_edit_film, name='admin_edit_film'),
    path('admin-panel/films/delete/<int:id>/', views.admin_delete_film, name='admin_delete_film'),


    path('admin-panel/salles/', views.admin_salles, name='admin_salles'),
    path('admin-panel/salles/add/', views.admin_add_salle, name='admin_add_salle'),
    path('admin-panel/salles/edit/<int:id>/', views.admin_edit_salle, name='admin_edit_salle'),
    path('admin-panel/salles/delete/<int:id>/', views.admin_delete_salle, name='admin_delete_salle'),

  
    path('admin-panel/representations/', views.admin_reps, name='admin_reps'),
    path('admin-panel/representations/add/', views.admin_add_rep, name='admin_add_rep'),
    path('admin-panel/representations/edit/<int:id>/', views.admin_edit_rep, name='admin_edit_rep'),
    path('admin-panel/representations/delete/<int:id>/', views.admin_delete_rep, name='admin_delete_rep'),
]
