from django.db import models
from datetime import datetime
import uuid

class Project(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(blank=True, max_length=100)

class Person(models.Model):
    def __str__(self):
        return self.name
    def end_snippet(self):
        self.current_snippet.stop_time = datetime.datetime.now()
        self.current_snippet = Null
    name = models.CharField(blank=True, max_length=100)
    private_id = models.UUIDField(default=uuid.uuid4)
    current_snippet = models.ForeignKey('Time', null=True)

class Time(models.Model):
    def __str__(self):
        return self.project.name + " " + str(self.start_time)
    start_time = models.DateTimeField(blank=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    person_safe = models.ForeignKey('Person')
    project = models.ForeignKey('Project')
