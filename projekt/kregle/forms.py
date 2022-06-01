from django import forms
from django.forms import ModelForm
from .models import Klub
from .models import Zawodnik
from .models import Rezerwacja

class KlubForm(ModelForm):
    class Meta:
        model = Klub
        fields = "__all__"
        

class ZawodnikForm(ModelForm):
    class Meta:
        model = Zawodnik
        fields = "__all__"
        labels = {
            'imie': '', 
            'nazwisko': '', 
            'plec': '', 
            'pseudonim': '', 
            'nr_buta': '', 
            'nr_telefonu': '', 
        }
        widgets = {
            'imie': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'nazwisko': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            'plec': forms.Select(attrs={'placeholder': 'Płeć'}),
            'pseudonim': forms.TextInput(attrs={'placeholder': 'Pseudonim'}),
            'nr_buta': forms.NumberInput(attrs={'placeholder': 'Numer buta'}),
            'nr_telefonu': forms.NumberInput(attrs={'placeholder': 'Numer telefonu'}),
        }

class RezerwacjaForm(ModelForm):
    class Meta:
        model = Rezerwacja
        fields = "__all__"
        labels = {
            'rezerwujacy': '',
            'godziny': '',
            'dzien': '', 
            'tor': '', 
            'osoby': '', 
        }
        widgets = {
            'rezerwujacy': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'godziny': forms.Select(),
            'dzien': forms.DateInput(attrs={'type': 'date'}),
            'tor': forms.Select(),
            'osoby': forms.Select(),
        }