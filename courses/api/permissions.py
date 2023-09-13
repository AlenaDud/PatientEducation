from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    """Check course enrollment. """
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
