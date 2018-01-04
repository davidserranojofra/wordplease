from rest_framework.permissions import BasePermission


class UsuariosPermisos(BasePermission):

    def has_permission(self, request, view):
        from usuarios.api import UsuarioDetalleAPI

        if request.method == 'POST' or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == 'GET' and isinstance(view, UsuarioDetalleAPI):
            return True

        return request.user.is_authenticated and (request.method == 'PUT' or request.method == 'DELETE')


    def has_object_permission(self, request, view, obj):

        return request.user == obj or request.user.is_superuser