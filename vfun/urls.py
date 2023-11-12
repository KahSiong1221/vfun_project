from django.urls import path
from django.views.generic.base import TemplateView
from .views import RegisterView, profile, get_halls


urlpatterns = [
    path('', TemplateView.as_view(template_name="vfun/home.html"), name='vfun-home'),
    path('register/', RegisterView.as_view(), name='vfun-register'),
    path('profile/', profile, name='vfun-profile'),
    path("get_halls/", get_halls, name="get_halls"),
]
