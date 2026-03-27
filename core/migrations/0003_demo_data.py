from django.db import migrations
from datetime import datetime, timedelta


def add_demo_data(apps, schema_editor):
    Technologie = apps.get_model('core', 'Technologie')
    Film = apps.get_model('core', 'Film')
    Salle = apps.get_model('core', 'Salle')
    Representation = apps.get_model('core', 'Representation')

    # Technologies (déjà créées en 0002, on les récupère)
    num = Technologie.objects.get(nom='Numérique')
    td3 = Technologie.objects.get(nom='3D')
    imax = Technologie.objects.get(nom='IMAX')
    fdx = Technologie.objects.get(nom='4DX')

    # ── Salles ──
    s1 = Salle.objects.create(nom='Salle 1 — Numérique', nombre_places=120)
    s1.technologies.set([num])

    s2 = Salle.objects.create(nom='Salle 2 — 3D', nombre_places=90)
    s2.technologies.set([num, td3])

    s3 = Salle.objects.create(nom='Salle 3 — IMAX', nombre_places=200)
    s3.technologies.set([num, imax])

    s4 = Salle.objects.create(nom='Salle 4 — 4DX', nombre_places=60)
    s4.technologies.set([num, td3, fdx])

    # ── Films ──
    f1 = Film.objects.create(
        titre='Les Gardiens de la Galaxie',
        description='Un groupe de criminels intergalactiques doit s\'unir pour arrêter un fanatique cosmique dont les plans meurtriers menacent l\'univers entier.',
        categorie='Action'
    )
    f1.technologies.set([num, td3])

    f2 = Film.objects.create(
        titre='Le Monde de Nemo 2',
        description='Nemo et ses amis vivent de nouvelles aventures sous-marines remplies de couleurs et d\'émotions. Un film pour toute la famille.',
        categorie='Enfants'
    )
    f2.technologies.set([num, td3])

    f3 = Film.objects.create(
        titre='Interstellar : Retour aux étoiles',
        description='Un astronaute embarque dans un voyage épique à travers un trou de ver pour trouver une nouvelle planète habitable avant que la Terre ne périsse.',
        categorie='Science-fiction'
    )
    f3.technologies.set([num, imax])

    f4 = Film.objects.create(
        titre='La Grande Aventure',
        description='Un voyage palpitant à travers des mondes fantastiques avec des effets spéciaux à couper le souffle. Vivez l\'expérience 4DX ultime.',
        categorie='Aventure'
    )
    f4.technologies.set([num, td3, fdx])

    f5 = Film.objects.create(
        titre='Comédie Royale',
        description='Une comédie hilarante sur un roi qui perd sa couronne et doit retrouver sa place parmi ses sujets. Rires garantis pour toute la famille.',
        categorie='Comédie'
    )
    f5.technologies.set([num])

    # ── Représentations (today + tomorrow) ──
    from django.utils import timezone
    now = timezone.now().replace(minute=0, second=0, microsecond=0)
    today = now.replace(hour=0)

    reps = [
        # Salle 1 — film numérique
        (f1, s1, today.replace(hour=10, minute=0)),
        (f1, s1, today.replace(hour=13, minute=0)),
        (f5, s1, today.replace(hour=16, minute=0)),
        (f5, s1, today.replace(hour=19, minute=30)),
        # Salle 2 — 3D
        (f2, s2, today.replace(hour=10, minute=0)),
        (f2, s2, today.replace(hour=14, minute=0)),
        (f4, s2, today.replace(hour=17, minute=30)),
        (f4, s2, today.replace(hour=20, minute=30)),
        # Salle 3 — IMAX
        (f3, s3, today.replace(hour=11, minute=0)),
        (f3, s3, today.replace(hour=15, minute=0)),
        (f3, s3, today.replace(hour=19, minute=0)),
        # Salle 4 — 4DX
        (f4, s4, today.replace(hour=12, minute=0)),
        (f4, s4, today.replace(hour=16, minute=0)),
        (f4, s4, today.replace(hour=20, minute=0)),
        # Lendemain
        (f1, s1, today.replace(hour=10, minute=0) + timedelta(days=1)),
        (f3, s3, today.replace(hour=14, minute=0) + timedelta(days=1)),
        (f2, s2, today.replace(hour=11, minute=0) + timedelta(days=1)),
    ]

    for film, salle, dt in reps:
        Representation.objects.create(film=film, salle=salle, date_heure=dt)


def remove_demo_data(apps, schema_editor):
    Film = apps.get_model('core', 'Film')
    Salle = apps.get_model('core', 'Salle')
    Film.objects.all().delete()
    Salle.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_initial_data'),
    ]
    operations = [
        migrations.RunPython(add_demo_data, remove_demo_data),
    ]
