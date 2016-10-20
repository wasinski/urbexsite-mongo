from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_mongoengine.routers import DefaultRouter as MongoDefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from users.views import UserCreationFormViewSet, register_confirm
from sites.views import SiteViewSet

drf_router = DefaultRouter()
mongo_router = MongoDefaultRouter()

drf_router.register(r'users', UserCreationFormViewSet)
mongo_router.register(r'sites', SiteViewSet)

urlpatterns = [
    url(r'^', include(drf_router.urls)),
    url(r'^', include(mongo_router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^confirm/(?P<activation_key>[0-9a-z-]+)/', register_confirm, name='activation'),
    url(r'^api-token-auth/', obtain_jwt_token, name='token-auth'),
    url(r'^api-token-verify/', verify_jwt_token, name='token-verify'),
]
