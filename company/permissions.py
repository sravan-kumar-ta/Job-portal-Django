from rest_framework.permissions import BasePermission


class IsCompanyOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return True

        if view.action in ['create', 'update', 'partial_update']:
            return request.user.role in ['admin', 'company']

        return False


class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "company"
