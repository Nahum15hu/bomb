from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, HttpRequest
from .models import Airfields, Budapest, Hungary, BombSites
from django.contrib.gis.geos import point

# Create your views here.
def home(request):
    return render(request, 'index.html', {
        'title': 'Kezdőoldal'
    })
    
def airfields_dataset(request):
    airfields = serialize('geojson', Airfields.objects.all())
    return HttpResponse(airfields, content_type='json')

def bombsites_dataset(request):
    bombsites = serialize('geojson', BombSites.objects.all())
    return HttpResponse(bombsites, content_type='json')

def budapest_dataset(request):
    budapest = serialize('geojson', Budapest.objects.all())
    return HttpResponse(budapest, content_type='json')

def hungary_dataset(request):
    hungary = serialize('geojson', Hungary.objects.all())
    return HttpResponse(hungary, content_type='json')