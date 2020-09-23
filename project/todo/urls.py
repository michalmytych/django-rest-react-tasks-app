from django.urls import path, include

from . import api_views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'todos', api_views.ThingToDoViewSet)
router.register(r'projects', api_views.ProjectToDoViewSet)
router.register(r'users', api_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]