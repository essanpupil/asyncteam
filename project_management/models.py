from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_creator')
    member = models.ManyToManyField(User, related_name='project_member')
    start = models.DateTimeField(default=now)
    end = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    assign_to = models.ManyToManyField(User)

    def __str__(self):
        return self.name
