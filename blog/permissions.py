from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede ejecutar el método o acceder a la vista/controlador que quiere acceder
        :param request:
        :param view:
        :return:
        """
        if view.action == "create" and not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        """
        Define si un usuario puede ejecutar la operación que quiere sobre el objeto 'obj'
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if view.action == "retrieve":
            return True

        return request.user.is_superuser or request.user == obj.owner