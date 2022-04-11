from rest_framework import permissions



class IsSuperuserOrStaffOrReadOnly(permissions.BasePermission):
 
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only staffs or superusers can use unsafe methods.
        user = request.user
        return user.is_authenticated and (user.is_staff or user.is_superuser)