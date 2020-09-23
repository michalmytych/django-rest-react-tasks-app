from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets

from .models import ThingToDo, ProjectToDo
from .serializers import ThingToDoSerializer, UserSerializer, ProjectToDoSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
        Class for viewing User objects queryset.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ThingToDoViewSet(viewsets.ModelViewSet):
    """
        Viewset for ProjectToDo - model for collection of ThingToDo objects.
    """
    queryset = ThingToDo.objects.all()
    serializer_class = ThingToDoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectToDoViewSet(viewsets.ModelViewSet):
    """
        Viewset for ProjectToDo - model for collection of ThingToDo objects.
    """
    queryset = ProjectToDo.objects.all()
    serializer_class = ProjectToDoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)