from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import ThingToDo, ProjectToDo



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
    todos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        new_user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'todos',
        )