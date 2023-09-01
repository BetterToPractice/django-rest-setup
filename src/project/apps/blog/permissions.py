from rest_framework import permissions


class PostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user)

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
