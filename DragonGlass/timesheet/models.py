from django.db import models

class Project(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(blank=True, max_length=100)

class Person(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(blank=True, max_length=100)
    current_snippet = models.ForeignKey('Time', null=True)

class Time(models.Model):
    def __str__(self):
        return self.project.name + " " + str(self.start_time)
    start_time = models.DateTimeField(blank=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    person_safe = models.ForeignKey('Person')
    project = models.ForeignKey('Project')
