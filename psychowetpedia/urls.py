from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leczenie/', views.treatment, name='treatment'),
    path('leczenie/psy/', views.dogs, name='dogs'),
    path('leczenie/psy/<str:uuid>/', views.treatment_dogs, name='treatment_dogs'),
    path('leczenie/koty/', views.cats, name='cats'),
    path('leczenie/koty/<str:uuid>/', views.treatment_cats, name='treatment_cats'),
    path('leki/', views.drug_index, name='drug_index'),
    path('lek/<str:uuid>/', views.single_drug, name='single_drug'),
]