from django.http import HttpResponse #delete??
from django.shortcuts import render, get_object_or_404
from .models import Project, Person, Time

def index(request):
    return render(request, 'index.html', {'Person':Person.objects, 'Time':Time.objects})
