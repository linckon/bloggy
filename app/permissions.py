from rest_framework import permissions

class DeletedReadOnly(permissions.BasePermission):
    message = "Deleted entries are read-only"

    def has_object_permission(self, request, view, obj):
        if obj.deleted and request.method not in permissions.SAFE_METHODS:
            return False
        return True


class IsTarget(permissions.BasePermission):
    message = "You are not allowed to read this notification."

    def has_object_permission(self, request, view, obj):
        return request.user.pk == obj.target.pk and request.method not in ['DELETE']

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "Not an owner."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user


class DisallowVoteChanges(permissions.BasePermission):
    message = "Can't update votes."

    def has_object_permission(self, request, view, obj):
        if request.data.get("downvotes") or request.data.get("upvotes"):
            return False
        return True
