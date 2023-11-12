from django.urls import path
from .views import home, RegisterView, profile

urlpatterns = [
    path('', home, name='vfun-home'),
    path('register/', RegisterView.as_view(), name='vfun-register'),
    path('profile/', profile, name='vfun-profile'),
]
