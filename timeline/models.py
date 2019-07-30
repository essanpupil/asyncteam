from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Flow(models.Model):
    name = models.CharField(max_length=255, default="Master Timeline")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_master = models.BooleanField(default=True)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mark(models.Model):
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE)
    time = models.DateTimeField(default=now)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
