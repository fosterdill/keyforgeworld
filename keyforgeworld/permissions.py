from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
      if request.method in SAFE_METHODS:
        return True

      return obj.get_owner() == request.user
