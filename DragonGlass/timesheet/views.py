from django.http import HttpResponse #delete??
from django.shortcuts import render, get_object_or_404
from .models import Project, Person, Time

def index(request, private_id):
    person   = get_object_or_404(Person, private_id = private_id)
    projects = Project.objects.all()
    if request.method == "POST":
        dostuff = request.POST["dostuff"]
        if dostuff == "stop":
            person.end_snippet()
        else:
            project_id = request.POST["project"]
            person.start_snippet(Project.objects.all().get(id = project_id))

    return render(request, 'index.html', {'Person':person, 'Time':Time.objects, 'Project':Project.objects.all()})
