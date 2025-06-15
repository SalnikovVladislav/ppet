from rest_framework.permissions import BasePermission
from apps.users.services.rbac import has_role

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return has_role(request.user, ['admin'])

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return has_role(request.user, ['manager'])

class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return has_role(request.user, ['employer'])

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return has_role(request.user, ['client'])
