from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.views import LoginView, LogoutView, SignupView

routerUsers = DefaultRouter()
routerUsers.register('api/1.0/users', UserViewSet)

urlpatterns = [
    # Web URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup', SignupView.as_view(), name='users_signup'),

    #API URL's
    url(r'', include(routerUsers.urls)),
]