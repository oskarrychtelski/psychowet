from django.urls import path
from . import views

urlpatterns = [
    path('', views.psychowetpedia, name='psychowetpedia'),
    path('psy/', views.psy, name='psy'),
    path('psy/<str:pk>/', views.leczenie_zaburzen_psy, name='leczenie_zaburzen_psy'),
    path('koty/', views.koty, name='koty'),
    path('koty/<str:pk>/', views.leczenie_zaburzen_koty, name='leczenie_zaburzen_koty')
]