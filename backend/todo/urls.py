from django.urls import path

from todo import api

"""
users_list = api.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
"""

urlpatterns = [
    path('current_user/', api.current_user),
    path('users/', api.UserList.as_view()),
    # path('users/', users_list, name="users_list"),
    path('todos/', api.todos_list, name="todos_list"),
    path('todos/<int:pk>/', api.todo_detail, name="todo_detail"),
]
