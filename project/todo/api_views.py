from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics
from rest_framework.response import Response

from .models import ThingToDo
from .serializers import ThingToDoSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    """
        Class for viewing User objects queryset.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetail(generics.RetrieveAPIView):
    """
        Class for viewing single User object data.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class ToDoList(generics.ListCreateAPIView):
    """
        Class for viewing ThingToDo objects queryset.
    """
    queryset = ThingToDo.objects.all()
    serializer_class = ThingToDoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def todo_detail(request, pk):
    """
        Function for getting, editing and deleting single ThingToDo object.
    """
    try:
        todo = ThingToDo.objects.get(id=pk)
    except ThingToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ThingToDoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ThingToDoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo = ThingToDo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
