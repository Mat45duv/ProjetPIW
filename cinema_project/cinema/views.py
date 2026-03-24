from django.shortcuts import render
from datetime import datetime
import sys
import django


FILMS = [
    {
        'nom': "Forrest Gump", 
        'date': '05/02/2026', 
        'heure': '20:00', 
        'salle': '1', 
        'categorie': 'Drame',
        'description': 'Témoin de nombreux événements marquants des années 60 et 70, un homme simple d\'esprit et au grand cœur inspire ceux qui l\'entourent à travers son optimisme constant.',
        'image': 'https://mlpnk72yciwc.i.optimole.com/cqhiHLc.IIZS~2ef73/w:auto/h:auto/q:75/https://bleedingcool.com/wp-content/uploads/2020/09/Forrest-Gump-Tom-Hanks.jpg',
        'meilleurVendeur': True
    },
    {
        'nom': "Bienvenue chez les Ch'tis", 
        'date': '06/02/2026', 
        'heure': '20:30', 
        'salle': '2', 
        'categorie': 'Comédie',
        'description': 'Un directeur de bureau de poste muté dans le Nord de la France découvre que les préjugés sur la région ne reflètent pas la réalité chaleureuse de ses habitants.',
        'image': 'https://img.lapresse.ca/924x615/201207/17/531046.jpg',
        'meilleurVendeur': False
    },
    {
        'nom': "Inception", 
        'date': '07/02/2026', 
        'heure': '19:00', 
        'salle': '3', 
        'categorie': 'Science-Fiction',
        'description': 'Un voleur spécialisé dans l\'extraction de secrets enfouis dans l\'inconscient tente une dernière mission : implanter une idée dans l\'esprit d\'un héritier.',
        'image': 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg',
        'meilleurVendeur': True
    },
    {
        'nom': "Le Fabuleux Destin d'Amélie Poulain", 
        'date': '08/02/2026', 
        'heure': '18:30', 
        'salle': '1', 
        'categorie': 'Romance',
        'description': 'Une jeune femme timide et rêveuse décide de consacrer sa vie à faire le bonheur des autres tout en cherchant le grand amour.',
        'image': 'https://m.media-amazon.com/images/M/MV5BNDg4NjM1YjMtYmNhZC00MjM0LWFiZmYtNGY1YjA3MzZmODc5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_.jpg',
        'meilleurVendeur': False
    },
    {
        'nom': "Les Intouchables", 
        'date': '09/02/2026', 
        'heure': '21:00', 
        'salle': '2', 
        'categorie': 'Comédie Dramatique',
        'description': 'L\'amitié improbable entre un aristocrate tétraplégique et son aide-soignant issu d\'un quartier défavorisé transforme leurs vies.',
        'image': 'https://m.media-amazon.com/images/M/MV5BMTYxNDA3MDQwNl5BMl5BanBnXkFtZTcwNTU4Mzc1Nw@@._V1_.jpg',
        'meilleurVendeur': True
    },
    {
        'nom': "La La Land", 
        'date': '10/02/2026', 
        'heure': '19:30', 
        'salle': '3', 
        'categorie': 'Comédie Musicale',
        'description': 'Une actrice en devenir et un pianiste de jazz tombent amoureux à Los Angeles tout en poursuivant leurs rêves respectifs.',
        'image': 'https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg',
        'meilleurVendeur': False
    },
]



def films(request):
    """Vue pour la page des films"""
    context = {
        'films': FILMS,
        'date_actuelle': datetime.now(),
    }
    return render(request, 'cinema/films.html', context)




def accueil(request):

    context = {
        'date_actuelle': datetime.now(),

    }
    return render(request, 'cinema/accueil.html', context)


def a_propos(request):
    context = {
        'date_actuelle': datetime.now(),
        'python_version': sys.version.split()[0],
        'django_version': django.get_version(),
        'bootstrap_version': '5.3.2',
        'ide': 'Visual Studio Code / Cursor',
        'nom_etudiant': 'Mathis et Landry',
        'numero_etudiant': 'N/A',
        'cours': 'Développement Web',
        'travail': 'Projet Cinéma',
        'date_remise': datetime.now().strftime('%d/%m/%Y'),
        'cegep': 'Cégep de La Pocatière',
    }
    return render(request, 'cinema/a_propos.html', context)


def documentation(request):
    ameliorations = [
        {
            'titre': 'Structure modulaire avec Django',
            'description': 'Implémentation d\'une architecture Django propre avec séparation des vues, URLs et templates. Utilisation de l\'héritage de templates pour éviter la duplication de code.'
        },
        {
            'titre': 'Design responsive avec Bootstrap 5',
            'description': 'Intégration de Bootstrap 5 pour un design responsive et moderne. Le site s\'adapte automatiquement aux différentes tailles d\'écran (mobile, tablette, desktop).'
        },
        {
            'titre': 'Gestion des films dynamique',
            'description': 'Affichage dynamique des films avec leurs informations complètes (titre, date, heure, salle, catégorie, description, image). Gestion des meilleurs vendeurs avec affichage conditionnel.'
        },
        {
            'titre': 'Navigation intuitive',
            'description': 'Menu de navigation avec indication de la page active. Liens vers toutes les sections du site (Accueil, Films, Documentation, À Propos).'
        },
        {
            'titre': 'Pied de page informatif',
            'description': 'Pied de page avec adresse du cinéma, date actuelle et informations de contact. Design cohérent avec le reste du site.'
        },
    ]
    
    context = {
        'date_actuelle': datetime.now(),
        'ameliorations': ameliorations,
    }
    return render(request, 'cinema/documentation.html', context)
