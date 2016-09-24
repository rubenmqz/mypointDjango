from django.contrib.auth.models import User
from rest_framework import mixins, viewsets

from users.permissions import UserPermission
from users.serializers import UserSerializer


class CreateRetrieveUpdateDestroyViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class UserViewSet(CreateRetrieveUpdateDestroyViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer
    permission_classes = (UserPermission,)