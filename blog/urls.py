from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from blog.views import HomeView, NewPostView, PostDetailView, PostsByUserView, BlogListView
from blog.api import BlogViewSet, PostViewSet, PostsByUserViewSet

routerBlogs = DefaultRouter()
routerBlogs.register('api/1.0/blogs', BlogViewSet)

routerPosts = DefaultRouter()
routerPosts.register('api/1.0/posts', PostViewSet)


urlpatterns = [
    # Web URLs
    url(r'^$', HomeView.as_view(), name='site_home'),
    url(r'^new-post$', NewPostView.as_view(), name='blog_new_post'),
    url(r'^blogs\/$', BlogListView.as_view(), name='blog_blogs'),
    url(r'^blogs\/(?P<nombre_de_usuario>[A-Za-z0-9.\+@_-]+)\/$', PostsByUserView.as_view(), name='blog_posts_by_user'),
    url(r'^blogs\/(?P<nombre_de_usuario>[A-Za-z0-9.\+@_-]+)\/(?P<post_id>[0-9]+)$', PostDetailView.as_view(), name='blog_post_detail'),

    #API URL's
    url(r'', include(routerBlogs.urls)),
    url(r'^api/1.0/posts/(?P<nombre_de_usuario>(?![0-9]+)[A-Za-z0-9.\+@_-]+)/$', PostsByUserViewSet.as_view({'get': 'list'}),
        name='api_blog_posts_by_user'),
    url(r'', include(routerPosts.urls)),

]