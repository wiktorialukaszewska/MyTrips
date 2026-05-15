from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'address', 'notes', 'trip']
        # latitude i longitude będą uzupełniane automatycznie przez JavaScript