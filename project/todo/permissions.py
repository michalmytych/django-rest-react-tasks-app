from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Class borrowed from DRF official documentation.
        'Custom permission to only allow owners of an object to edit it.'
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsOwnerOrStaff(permissions.BasePermission):
    """
        Only creators of objects, or staff members can view or modify them.
    """
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.is_staff:
            return True
        else:
            return False