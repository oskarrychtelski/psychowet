from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('notatki/', views.notes, name='notes'),
    path('stworz-notatke/', views.createNotes, name='createNotes'),
    path('edytuj-notatke/<str:uuid>', views.updateNotes, name='updateNotes'),
    path('usun-notatke/<str:uuid>', views.deleteNotes, name='deleteNotes'),

    path('kontakt/', views.contact, name='contact')
]