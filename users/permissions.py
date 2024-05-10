from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Проверка активности сотрудника.
    """

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return True

        return False
