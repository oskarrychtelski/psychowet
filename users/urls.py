from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('notatki/', views.notes, name='notes'),
    path('stworz_notatke/', views.createNotes, name='createNotes')
]