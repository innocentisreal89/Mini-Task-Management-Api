from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #allow only read only method for everyone
            return True
        # check if the user making the request is the owner of the todo
        return obj.user == request.user