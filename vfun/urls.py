from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'sportshalls', views.SportsHallViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'mysportshalls', views.UserSportsHallViewSet, basename='mysportshalls')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
