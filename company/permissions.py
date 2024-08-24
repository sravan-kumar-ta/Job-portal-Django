from rest_framework.permissions import BasePermission


class IsCompanyOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'retrieve':
            return True

        if view.action in ['create', 'update', 'list']:
            return request.user.role in ['admin', 'company']

        return False
