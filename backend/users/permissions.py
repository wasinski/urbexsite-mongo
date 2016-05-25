from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # check if user is owner
        return request.user == obj
