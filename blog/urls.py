from django.conf.urls import url

from blog.views import HomeView, NewPostView, PostDetailView

urlpatterns = [
    # Web URLs
    url(r'^$', HomeView.as_view(), name='site_home'),
    url(r'^new-post$', NewPostView.as_view(), name='blog_new_post'),
    url(r'^blogs\/(?P<nombre_de_usuario>[A-Za-z0-9.\+@_-]+)\/(?P<post_id>[0-9]+)$', PostDetailView.as_view(), name='blog_post_detail'),
]