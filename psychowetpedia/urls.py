from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('psy/', views.psy, name='psy'),
    path('psy/<str:uuid>/', views.leczenie_zaburzen_psy, name='leczenie_zaburzen_psy'),
    path('koty/', views.koty, name='koty'),
    path('koty/<str:uuid>/', views.leczenie_zaburzen_koty, name='leczenie_zaburzen_koty'),
    path('leki/', views.leki, name='leki'),
    path('lek/<str:uuid>/', views.lek, name='lek'),
]