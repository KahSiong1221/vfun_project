from django.urls import path
from .views import home, RegisterView, profile
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="vfun/home.html"), name='vfun-home'),
    path('register/', RegisterView.as_view(), name='vfun-register'),
    path('profile/', profile, name='vfun-profile'),
]
