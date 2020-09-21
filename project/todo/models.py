from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ThingToDo(models.Model):
    """
        Represents a thing to be done.
    """
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    added_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class ProjectToDo(models.Model):
    """
        Represents a set of things to be done.
    """
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    added_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

