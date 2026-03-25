from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, Salle, Representation
from .forms import ReservationForm


def accueil(request):
    return render(request, "base.html")


def liste_films(request):
    films = Film.objects.all()
    return render(request, "films.html", {"films": films})


def representations_film(request, film_id):
    reps = Representation.objects.filter(film_id=film_id)
    return render(request, "representations.html", {"reps": reps})


def detail_representation(request, id):
    rep = get_object_or_404(Representation, id=id)
    return render(request, "representation_detail.html", {"rep": rep})


def reserver(request, id):
    rep = get_object_or_404(Representation, id=id)

    if request.method == "POST":
        form = ReservationForm(request.POST, representation=rep)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.representation = rep
            reservation.save()
            return redirect("confirmation")

    else:
        form = ReservationForm(representation=rep)

    return render(request, "reserver.html", {
        "form": form,
        "rep": rep
    })

def confirmation(request):
    return render(request, "confirmation.html")

# Admin
def admin_dashboard(request):
    return render(request, "admin/dashboard.html")


def admin_films(request):
    films = Film.objects.all()
    return render(request, "admin/films.html", {"films": films})

def admin_add_film(request):
    if request.method == "POST":
        Film.objects.create(
            titre=request.POST["titre"],
            description=request.POST["description"],
            categorie=request.POST["categorie"]
        )
        return redirect("admin_films")

    return render(request, "admin/add_film.html")

def admin_edit_film(request, id):
    film = get_object_or_404(Film, id=id)

    if request.method == "POST":
        film.titre = request.POST["titre"]
        film.description = request.POST["description"]
        film.categorie = request.POST["categorie"]
        film.save()
        return redirect("admin_films")

    return render(request, "admin/edit_film.html", {"film": film})

def admin_delete_film(request, id):
    film = get_object_or_404(Film, id=id)
    film.delete()
    return redirect("admin_films")

def admin_salles(request):
    salles = Salle.objects.all()
    return render(request, "admin/salles.html", {"salles": salles})


def admin_reps(request):
    reps = Representation.objects.all()
    return render(request, "admin/reps.html", {"reps": reps})

#TODO admin crud
