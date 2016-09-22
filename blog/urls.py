from django.conf.urls import url

from blog.views import HomeView

urlpatterns = [
    # Web URLs
    url(r'^$', HomeView.as_view(), name='site_home'),
]