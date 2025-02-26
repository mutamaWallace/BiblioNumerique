from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsWallaceAdmin(BasePermission):
    """
    Permission pour permettre uniquement à l'utilisateur 'wallace' d'accéder à l'API.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.username == 'wallace'