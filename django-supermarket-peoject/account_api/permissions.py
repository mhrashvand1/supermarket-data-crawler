from rest_framework import permissions

class IsSuperuser(permissions.BasePermission):
 
    def has_permission(self, request, view):
        # only superusers have permission
        user = request.user
        return user.is_authenticated and user.is_superuser


