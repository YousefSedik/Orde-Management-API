from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.user.is_superuser or request.user == obj.owner:
            return True

        return False
    