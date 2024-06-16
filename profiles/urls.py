from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        'reset_password/',
        views.password_reset_request,
        name='password_reset_request'
    ),
    path(
        'change_password/<uidb64>/<token>/',
        views.password_change,
        name='password_change'
    ),
    path(
        'reset_password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
]
