from django.urls import path
from .views import home, RegisterView

urlpatterns = [
    path('', home, name='vfun-home'),
    path('register/', RegisterView.as_view(), name='vfun-register'),
]
