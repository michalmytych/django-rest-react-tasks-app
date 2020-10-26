from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class ThingToDo(models.Model):
    """
        Represents a To-Do task.
    """
    class Meta:
        ordering = ['-created_at']
        db_table = 'thing_to_do'

    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), related_name='todos', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'ThingToDo: "{self.name}"'
