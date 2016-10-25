from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_mongoengine.routers import DefaultRouter as MongoDefaultRouter

from locations.views import LocationViewSet

drf_router = DefaultRouter()
mongo_router = MongoDefaultRouter()

# drf_router.register(r'users', UserCreationFormViewSet)
mongo_router.register(r'locations', LocationViewSet)

urlpatterns = [
#   url(r'^api/', include(drf_router.urls)),
    url(r'^api/', include(mongo_router.urls)),
    url(r'^api/accounts/', include('rest_auth.urls')),
    url(r'^api/accounts/registration/', include('rest_auth.registration.urls')),
    url(r'^admin/', admin.site.urls),
]
