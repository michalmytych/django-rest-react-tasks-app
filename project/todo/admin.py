from django.contrib import admin

from .models import ThingToDo, ProjectToDo


admin.site.register(ThingToDo)
admin.site.register(ProjectToDo)
