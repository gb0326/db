from django.shortcuts import render
from django.views import View
from collections import OrderedDict
from .fusioncharts import FusionCharts
from .models import Crime

# Create your views here.
def arrest(request) :
    return render(request, 'data/arrest.html')
def location(request) :
    return render(request, 'data/location.html')
def safemap(request) :
    return render(request, 'data/safemap.html')
def region(request) :
    return render(request, 'data/region.html')

def index(request) :
    data = Crime.objects.all()
    return render(request, 'data/arrest.html', {'crime_list' : data})
    

