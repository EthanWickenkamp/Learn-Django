from django.urls import path, include
from rest_framework import routers

from .views import ItemViewSet, TeamViewSet, GameViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'games', GameViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]