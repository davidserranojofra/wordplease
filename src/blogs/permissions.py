from rest_framework.permissions import BasePermission


class PostPermisos(BasePermission):

    def has_permission(self, request, view):
        return request.method == 'GET' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method == 'GET' or obj.usuario == (request.user or request.is_superuser)


class PostDetallesPermisos(BasePermission):

    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):
        pass