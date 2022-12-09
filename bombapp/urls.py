from django.urls import include, path
import django.contrib.auth.views

from bombapp import views
from .models import Airfields, BombSites, Budapest, Hungary

urlpatterns = [
    path('', views.home, name='home'),
    path('airfields/', views.airfields_dataset, name="airfields"),
    path('bombsites/', views.bombsites_dataset, name="bombsites"),
    path('budapest/', views.budapest_dataset, name="budapest"),
    path('hungary/', views.hungary_dataset, name="hungary"),
]