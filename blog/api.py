from django.contrib.auth.models import User
from rest_framework import mixins, viewsets, filters

from blog.serializers import BlogSerializer
from blog.views import BlogQuerySet



class ListViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    Un viewset que proporciona la acciones 'list'.
    """
    pass


class BlogViewSet(ListViewSet):

    queryset = BlogQuerySet.get_blogs_with_content()
    serializer_class = BlogSerializer
    search_fields = ('username',)
    order_fields = ('first_name',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

