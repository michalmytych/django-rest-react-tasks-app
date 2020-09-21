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
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('ProjectToDo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'thing_to_do'


class ProjectToDo(models.Model):
    """
        Represents a set of things to be done.
    """
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_to_do'

