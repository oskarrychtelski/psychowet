from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Notatki


class NotesForm(ModelForm):
    class Meta:
        model = Notatki
        fields = ['imie_zwierzecia', 'zaburzenie', 'lek', 'opis']


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         labels = {
#             'username': 'Nazwa Użytkownika',
#             'email': 'Adres e-mail',
#             'password1': 'Hasło',
#             'password2': 'Powtórz hasło'
#         }