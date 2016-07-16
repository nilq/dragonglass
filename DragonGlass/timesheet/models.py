from django.db import models
from datetime import datetime
import uuid

class Team(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(blank=True, max_length=100)

class Project(models.Model):
    team = models.ForeignKey(Team)
    def __str__(self):
        return self.name
    name = models.CharField(blank=True, max_length=100)
    active = models.BooleanField(default=True)

class Person(models.Model):
    def __str__(self):
        return self.name
    def end_snippet(self):
        self.current_snippet.stop_time = datetime.now()
        self.current_snippet = None
    def start_snippet(self, project):
        temp = Time.objects.create(start_time=datetime.now, person_safe=self, project=project)
        self.current_snippet = temp

    name = models.CharField(blank=True, max_length=100)
    private_id = models.UUIDField(default=uuid.uuid4)

    project = models.ForeignKey(Project)

class Time(models.Model):
    def __str__(self):
        return self.project.name + " : " + str(self.start_time)

    start_time  = models.DateTimeField(editable = True, default = datetime.now)
    stop_time   = models.DateTimeField(null = True, default = None)

    person_safe = models.ForeignKey('Person')
    project     = models.ForeignKey('Project')
