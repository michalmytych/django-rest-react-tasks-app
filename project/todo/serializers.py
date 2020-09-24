from django.conf import settings

from rest_framework import serializers

from .models import ThingToDo, ProjectToDo

UserModel = settings.AUTH_USER_MODEL


class ThingToDoSerializer(serializers.ModelSerializer):
    """
        Class to serialize ThingToDo model for JSON api.
    """
    user = serializers.ReadOnlyField(source='user.username')

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
        Class to serialize ProjectToDo model for JSON api.
    """
    user = serializers.ReadOnlyField(source='user.username')

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
        Class to serialize built-in Django User model for JSON api.
    """
    todos = serializers.ReadOnlyField()

    class Meta:
        model = UserModel
        fields = (
            'id',
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'todos',
        )