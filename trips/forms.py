from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'address', 'notes']
        # trip jest ustawiany automatycznie z URL, nie pokazujemy go w formularzu