from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ThingToDo, ProjectToDo


class ThingToDoSerializer(serializers.ModelSerializer):
    """
        Meta class to serialize ThingToDo model for JSON api.
    """
    class Meta:
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
    """
        Meta class to serialize ProjectToDo model for JSON api.
    """
    class Meta:
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


class UserSerializer(serializers.ModelSerializer):
    """
        Meta class to serialize built-in Django User model for JSON api.
    """
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=ProjectToDo.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'todos'
        )