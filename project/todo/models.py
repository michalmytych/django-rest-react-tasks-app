from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class ThingToDo(models.Model):
    """
        Represents a To-Do task.
    """
    class Meta:
        db_table = 'thing_to_do'

    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(get_user_model(), related_name='todos', on_delete=models.CASCADE)
    project = models.ForeignKey('ProjectToDo', related_name='todos', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'ThingToDo: "{self.name}"'


class ProjectToDo(models.Model):
    """
        Represents a set of To-Do tasks with extra info.
    """
    class Meta:
        db_table = 'project_to_do'

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(get_user_model(), related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return f'ProjectToDo: "{self.title}"'

