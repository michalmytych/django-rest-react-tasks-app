from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ThingToDo
from .serializers import ThingToDoSerializer


@api_view(['GET', 'POST'])
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
            return Response(serializer.data)        # or 200 OK (but it's the same thing I guess)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo = ThingToDo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # I maybe should handle the exception "405 Method Not Allowed response"...


"""
    *** TO-DO ***
    
    1. Add views for:
        * todos of specific project 
        * all projects
        * specific project
"""