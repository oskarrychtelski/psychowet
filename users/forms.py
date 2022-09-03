from django.forms import ModelForm
from .models import Notatki


class NotesForm(ModelForm):
    class Meta:
        model = Notatki
        fields = ['imie_zwierzecia', 'zaburzenie', 'lek', 'opis']
