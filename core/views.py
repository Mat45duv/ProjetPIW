from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Film, Salle, Representation, Technologie
from .forms import ReservationForm

CATEGORIES = [
    'Enfants', 'Famille', 'Action', 'Comédie', 'Drame',
    'Horreur', 'Science-fiction', 'Aventure', 'Animation', 'Thriller'
]




def accueil(request):
    return render(request, 'accueil.html')


def liste_films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})


def representations_film(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    reps = Representation.objects.filter(film=film).order_by('date_heure')
    return render(request, 'representations.html', {'reps': reps, 'film': film})


def detail_representation(request, id):
    rep = get_object_or_404(Representation, id=id)
    return render(request, 'representation_detail.html', {'rep': rep})


def reserver(request, id):
    rep = get_object_or_404(Representation, id=id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, representation=rep)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.representation = rep
            reservation.save()
            return redirect('confirmation')
    else:
        form = ReservationForm(representation=rep)

    return render(request, 'reserver.html', {'form': form, 'rep': rep})


def confirmation(request):
    return render(request, 'confirmation.html')


def a_propos(request):
    return render(request, 'a_propos.html')




def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')




def admin_films(request):
    films = Film.objects.all()
    return render(request, 'admin/films.html', {'films': films})


def admin_add_film(request):
    technologies = Technologie.objects.all()
    if request.method == 'POST':
        film = Film.objects.create(
            titre=request.POST['titre'],
            description=request.POST['description'],
            categorie=request.POST['categorie'],
        )
        tech_ids = request.POST.getlist('technologies')
        film.technologies.set(tech_ids)
        messages.success(request, f'Le film « {film.titre} » a été ajouté avec succès.')
        return redirect('admin_films')
    return render(request, 'admin/add_film.html', {'technologies': technologies, 'categories': CATEGORIES})


def admin_edit_film(request, id):
    film = get_object_or_404(Film, id=id)
    technologies = Technologie.objects.all()
    if request.method == 'POST':
        film.titre = request.POST['titre']
        film.description = request.POST['description']
        film.categorie = request.POST['categorie']
        film.save()
        tech_ids = request.POST.getlist('technologies')
        film.technologies.set(tech_ids)
        messages.success(request, f'Le film « {film.titre} » a été modifié avec succès.')
        return redirect('admin_films')
    return render(request, 'admin/edit_film.html', {'film': film, 'technologies': technologies, 'categories': CATEGORIES})


def admin_delete_film(request, id):
    film = get_object_or_404(Film, id=id)
    titre = film.titre
    film.delete()
    messages.success(request, f'Le film « {titre} » a été supprimé.')
    return redirect('admin_films')




def admin_salles(request):
    salles = Salle.objects.all()
    return render(request, 'admin/salles.html', {'salles': salles})


def admin_add_salle(request):
    technologies = Technologie.objects.all()
    if request.method == 'POST':
        salle = Salle.objects.create(
            nom=request.POST['nom'],
            nombre_places=int(request.POST['nombre_places']),
        )
        tech_ids = request.POST.getlist('technologies')
        salle.technologies.set(tech_ids)
        messages.success(request, f'La salle « {salle.nom} » a été ajoutée avec succès.')
        return redirect('admin_salles')
    return render(request, 'admin/add_salle.html', {'technologies': technologies})


def admin_edit_salle(request, id):
    salle = get_object_or_404(Salle, id=id)
    technologies = Technologie.objects.all()
    if request.method == 'POST':
        salle.nom = request.POST['nom']
        salle.nombre_places = int(request.POST['nombre_places'])
        salle.save()
        tech_ids = request.POST.getlist('technologies')
        salle.technologies.set(tech_ids)
        messages.success(request, f'La salle « {salle.nom} » a été modifiée.')
        return redirect('admin_salles')
    return render(request, 'admin/edit_salle.html', {'salle': salle, 'technologies': technologies})


def admin_delete_salle(request, id):
    salle = get_object_or_404(Salle, id=id)
    nom = salle.nom
    salle.delete()
    messages.success(request, f'La salle « {nom} » a été supprimée.')
    return redirect('admin_salles')




def admin_reps(request):
    reps = Representation.objects.select_related('film', 'salle').order_by('date_heure')
    return render(request, 'admin/reps.html', {'reps': reps})


def admin_add_rep(request):
    films = Film.objects.all()
    salles = Salle.objects.all()
    error = None
    if request.method == 'POST':
        try:
            film = get_object_or_404(Film, id=request.POST['film_id'])
            salle = get_object_or_404(Salle, id=request.POST['salle_id'])
            rep = Representation(
                film=film,
                salle=salle,
                date_heure=request.POST['date_heure'],
            )
            rep.full_clean()
            rep.save()
            messages.success(request, 'La représentation a été créée avec succès.')
            return redirect('admin_reps')
        except ValidationError as e:
            error = ' '.join(e.messages)
    return render(request, 'admin/add_rep.html', {'films': films, 'salles': salles, 'error': error})


def admin_edit_rep(request, id):
    rep = get_object_or_404(Representation, id=id)
    films = Film.objects.all()
    salles = Salle.objects.all()
    error = None
    if request.method == 'POST':
        try:
            rep.film = get_object_or_404(Film, id=request.POST['film_id'])
            rep.salle = get_object_or_404(Salle, id=request.POST['salle_id'])
            rep.date_heure = request.POST['date_heure']
            rep.full_clean()
            rep.save()
            messages.success(request, 'La représentation a été modifiée avec succès.')
            return redirect('admin_reps')
        except ValidationError as e:
            error = ' '.join(e.messages)
    return render(request, 'admin/edit_rep.html', {'rep': rep, 'films': films, 'salles': salles, 'error': error})


def admin_delete_rep(request, id):
    rep = get_object_or_404(Representation, id=id)
    rep.delete()
    messages.success(request, 'La représentation a été supprimée.')
    return redirect('admin_reps')
