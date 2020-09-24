from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
    """
        Only creators of objects, or staff members can view or modify them.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user