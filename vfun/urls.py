from django.urls import path
from .views import RegisterView, profile, SportsHallMapView


urlpatterns = [
    path('', SportsHallMapView.as_view(), name='vfun-home'),
    path('register/', RegisterView.as_view(), name='vfun-register'),
    path('profile/', profile, name='vfun-profile'),
]
