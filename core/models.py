# type: ignore
from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta

class Technologie(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom


class Film(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    categorie = models.CharField(max_length=50)
    technologies = models.ManyToManyField(Technologie)

    def __str__(self):
        return self.titre


class Salle(models.Model):
    nom = models.CharField(max_length=50)
    nombre_places = models.IntegerField()
    technologies = models.ManyToManyField(Technologie)

    def __str__(self):
        return self.nom


class Representation(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()

    def billets_vendus(self):
        return sum(r.nombre_billets for r in self.reservation_set.all())

    def places_restantes(self):
        return self.salle.nombre_places - self.billets_vendus()

    def clean(self):
      
        reps = Representation.objects.filter(salle=self.salle)
        for r in reps:
            if r.id != self.id:
                diff = abs((r.date_heure - self.date_heure).total_seconds())
                if diff < 1800:
                    raise ValidationError("30 minutes entre projections requises")

       
        if not self.salle.technologies.filter(
            id__in=self.film.technologies.all()
        ).exists():
            raise ValidationError("Technologie incompatible salle/film")

    def __str__(self):
        return f"{self.film} - {self.date_heure}"


class Reservation(models.Model):
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=100)
    nombre_billets = models.IntegerField()
