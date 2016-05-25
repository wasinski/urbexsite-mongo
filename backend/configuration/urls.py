from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from users.views import UserCreationFormViewSet, register_confirm

router = DefaultRouter()

router.register(r'users', UserCreationFormViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^confirm/(?P<activation_key>[0-9a-z-]+)/', register_confirm, name='activation'),
    url(r'^api-token-auth/', obtain_jwt_token, name='token-auth'),
    url(r'^api-token-verify/', verify_jwt_token, name='token-verify'),
]
