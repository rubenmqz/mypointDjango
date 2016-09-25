from django.contrib.auth.models import User
from rest_framework import mixins, viewsets, filters
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response

from blog.models import Post
from blog.permissions import PostPermission
from blog.serializers import BlogSerializer, PostSerializer, FullPostSerializer
from blog.views import BlogQuerySet, PostsQuerySet


class CreateRetrieveUpdateDestroyViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
    Un viewset que proporciona las acciones 'retrieve', 'create', 'update' y 'destroy'.
    """
    pass


class ListViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    Un viewset que proporciona la acciones 'list'.
    """
    pass


class BlogViewSet(ListViewSet):
    """
    Endpoint de listado de blogs (= listado de usuarios que tienen posts)
    """
    queryset = BlogQuerySet.get_blogs_with_content()
    serializer_class = BlogSerializer
    search_fields = ('username',)
    order_fields = ('first_name',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)


class PostsByUserViewSet(ListViewSet):
    """
    Endpoint de listado de posts de un usuario
    """
    search_fields = ('title', 'summary',)
    order_fields = ('title', 'publish_at')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    serializer_class = PostSerializer

    def get_queryset(self):
        user = User.objects.filter(username=self.kwargs['nombre_de_usuario'])
        if len(user) == 0:
            return Response("El blog que buscas no existe", status=HTTP_404_NOT_FOUND)
        return PostsQuerySet.get_posts_by_user(user, self.request.user)


class PostViewSet(CreateRetrieveUpdateDestroyViewSet):

    queryset = Post.objects.all()

    serializer_class = FullPostSerializer
    permission_classes = (PostPermission,)

    def get_queryset(self):
        if self.action=="retrieve":
            return PostsQuerySet.get_post(self.kwargs['pk'], self.request.user)
        else:
            return Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
