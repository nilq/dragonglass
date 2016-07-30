from django.db import models
from datetime import datetime
import uuid

class Project(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

class Person(models.Model):
    def __str__(self):
        return self.name
    def end_snippet(self):
        self.current_snippet.stop()
        self.current_snippet = None
        self.save()
    def start_snippet(self, project):
        self.current_snippet = Time.objects.create(start_time=datetime.now(), person_safe=self, project=project)
        self.save()

    name = models.CharField(max_length=100)
    private_id = models.UUIDField(default=uuid.uuid4)

    current_snippet = models.ForeignKey('Time', blank=True, null=True)

class Time(models.Model):
    def __str__(self):
        return self.project.name + " : " + str(self.start_time)
    def stop(self):
        self.stop_time = datetime.now()
        self.save()

    start_time  = models.DateTimeField(editable = True, default = datetime.now)
    stop_time   = models.DateTimeField(null = True, blank = True, default = None)

    person_safe = models.ForeignKey('Person')
    project     = models.ForeignKey('Project')
