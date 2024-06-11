# profiles/urls.py
from django.urls import path
from .views import password_reset_request, password_reset_form

urlpatterns = [
    path('password_reset/', password_reset_request, name='password_reset_request'),
    path('password_reset_form/<int:user_id>/', password_reset_form, name='password_reset_form'),
]
