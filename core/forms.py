from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom_client', 'nombre_billets']

    def __init__(self, *args, **kwargs):
        self.representation = kwargs.pop('representation', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        nb = cleaned_data.get("nombre_billets")

        if self.representation and nb:
            if self.representation.places_restantes() < nb:
                raise forms.ValidationError("Pas assez de places disponibles")

        return cleaned_data
