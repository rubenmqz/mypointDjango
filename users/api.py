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
    Un viewset que proporciona las acciones 'retrieve', 'create', 'update' y 'destroy'.
    """
    pass


class UserViewSet(CreateRetrieveUpdateDestroyViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
