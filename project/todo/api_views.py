from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics
from rest_framework.response import Response

from .models import ThingToDo
from .serializers import ThingToDoSerializer, UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def todos_list(request):
    if request.method == 'GET':
        todos = ThingToDo.objects.all()
        serializer = ThingToDoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ThingToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def todo_detail(request, pk):
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
