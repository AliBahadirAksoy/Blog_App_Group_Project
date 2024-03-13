from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kullanıcı admin ise veya blogun sahibi ise izin ver
        return request.user.is_staff or obj.user == request.user