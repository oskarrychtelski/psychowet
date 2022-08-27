from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('psy/', views.dogs, name='dogs'),
    path('psy/<str:uuid>/', views.treatment_dogs, name='treatment_dogs'),
    path('koty/', views.cats, name='cats'),
    path('koty/<str:uuid>/', views.treatment_cats, name='treatment_cats'),
    path('leki/', views.drug_index, name='drug_index'),
    path('lek/<str:uuid>/', views.single_drug, name='single_drug'),
]