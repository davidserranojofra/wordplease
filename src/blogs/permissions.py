from rest_framework.permissions import BasePermission


class PostPermisos(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET' or request.user.is_superuser:
            return True


    def has_object_permission(self, request, view, obj):

        return request.user == obj or request.user.is_superuser



class PostDetallesPermisos(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated


    def has_object_permission(self, request, view, obj):

        return request.user == obj or request.user.is_superuser