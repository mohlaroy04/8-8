from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'DELETE']:
            return obj.author == request.user.username
        return True
