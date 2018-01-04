from rest_framework.permissions import BasePermission



class PostPermisos(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET' or request.user.is_superuser:
            return True


    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True

        if request.method == 'PUT' or request.method == 'DELETE' or request.method == 'GET':
            return obj.usuario == request.user or request.user.is_superuser