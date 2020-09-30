from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions

from .models import ThingToDo, ProjectToDo
from .serializers import ThingToDoSerializer, UserSerializer, ProjectToDoSerializer
from .permissions import IsOwnerOrStaff



class UserViewSet(viewsets.ModelViewSet):
    """
        Class for viewing User objects queryset.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ThingToDoViewSet(viewsets.ModelViewSet):
    """
        Viewset for ProjectToDo - model for collection of ThingToDo objects.
    """
    queryset = ThingToDo.objects.all()
    serializer_class = ThingToDoSerializer
    permission_classes = [IsOwnerOrStaff, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectToDoViewSet(viewsets.ModelViewSet):
    """
        Viewset for ProjectToDo - collection of ThingToDo objects.
    """
    queryset = ProjectToDo.objects.all()
    serializer_class = ProjectToDoSerializer
    permission_classes = [IsOwnerOrStaff, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)