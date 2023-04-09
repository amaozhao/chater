from rest_framework import permissions


class DialogOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class DialogLogOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.dialog.user == request.user
