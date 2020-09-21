from django.conf.urls import url
from django.urls import path
from . import views, api_views


urlpatterns = [
    # just a test view as url():
    url('test/', views.test, name='test'),
    # api views as paths():
    path('todos-list/', api_views.ToDoList.as_view(), name="todos_list"),
    path('todo-detail/<int:pk>/', api_views.todo_detail, name="todo_detail"),
    # api user views
    path('users/', api_views.UserList.as_view()),
    path('users/<int:pk>/', api_views.UserDetail.as_view()),
]
