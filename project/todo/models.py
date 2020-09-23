from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ThingToDo(models.Model):
    """
        Represents a thing to be done.
    """
    class Meta:
        db_table = 'thing_to_do'

    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    project = models.ForeignKey('ProjectToDo', on_delete=models.CASCADE)

    def __str__(self):
        return f'ThingToDo: "{self.name}"'


class ProjectToDo(models.Model):
    """
        Represents a set of things to be done.
    """
    class Meta:
        db_table = 'project_to_do'

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default_project = models.BooleanField(default=False)

    def __str__(self):
        return f'ProjectToDo: "{self.title}"'

