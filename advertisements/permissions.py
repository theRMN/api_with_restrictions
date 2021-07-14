from rest_framework import permissions


class IsOwnerPermissionOrIsAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator or bool(request.user and request.user.is_staff)
