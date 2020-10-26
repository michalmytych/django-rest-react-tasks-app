from django.core.exceptions import PermissionDenied

from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from .models import ThingToDo
from .serializers import ThingToDoSerializer, UserSerializer, UserSerializerWithToken


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET', 'POST'])
def todos_list(request):
    """
        List all to-do tasks. Also, authenticated user can create new tasks.
    """
    if request.method == 'GET':
        snippets = ThingToDo.objects.filter(user=request.user.id)
        serializer = ThingToDoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ThingToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def todo_detail(request, pk):
    """
        Retrieve, update or delete single to-do task.
    """
    try:
        todo = ThingToDo.objects.get(id=pk)
    except ThingToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if todo.user != request.user:
        raise PermissionDenied
    else:
        if request.method == 'GET':
            serializer = ThingToDoSerializer(todo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ThingToDoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PATCH':
            serializer = ThingToDoSerializer(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def current_user(request):
    """
        Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
        Create a new user. It's called 'UserList' because normally we'd have a get
        method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
