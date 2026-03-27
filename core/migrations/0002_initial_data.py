from django.db import migrations

def add_technologies(apps, schema_editor):
    Technologie = apps.get_model('core', 'Technologie')
    for nom in ['Numérique', '3D', 'IMAX', '4DX']:
        Technologie.objects.get_or_create(nom=nom)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_technologies, migrations.RunPython.noop),
    ]
