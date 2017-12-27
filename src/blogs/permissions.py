from rest_framework.permissions import BasePermission
from datetime import datetime

class PostPermisos(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET' or request.user.is_superuser:
            return True


    def has_object_permission(self, request, view, obj):

        if request.method == 'GET' and obj.fecha_publicacion > datetime.now():
            return False

        return obj.usuario == request.user or request.user.is_superuser



class PostDetallesPermisos(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        return obj.usuario == request.user or request.user.is_superuser