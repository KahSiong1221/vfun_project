from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.sportshall_list, name='sportshall_list'),
    path('sportshalls/', views.sportshall_list, name='sportshall_list'),
    path('mysportshalls/', views.my_sportshall_list, name='my_sportshall_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True,
                                                 template_name='vfun_frontend/login.html',
                                                 authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='vfun_frontend/logout.html'), name='logout'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='vfun_frontend/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='vfun_frontend/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
