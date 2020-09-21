from rest_framework import serializers
from .models import ThingToDo, ProjectToDo


class ThingToDoSerializer(serializers.ModelSerializer):
    class Meta:
        """
            Meta class to serialize ThingToDo model for JSON api.
        """
        model = ThingToDo
        fields = (
            'id',
            'name',
            'description',
            'deadline',
            'done',
            'created_at',
            'user',
            'project',
        )
        read_only_fields = ('created_at', 'id')


class ProjectToDoSerializer(serializers.ModelSerializer):
    class Meta:
        """
            Meta class to serialize ProjectToDo model for JSON api.
        """
        model = ProjectToDo
        fields = (
            'id',
            'title',
            'description',
            'deadline',
            'completed',
            'created_at',
            'user',
        )
        read_only_fields = ('created_at', 'id')