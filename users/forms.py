from django.forms import ModelForm
from .models import Notatki


class NotesForm(ModelForm):
    class Meta:
        model = Notatki
        fields = '__all__'
