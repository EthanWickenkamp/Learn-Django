from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloWorld
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('hello', HelloWorld.as_view(), name='hello'),
    path('', include(router.urls)),
]