from django.urls import path
from. import views

urlpatterns = [
    path('', views.clan_creation, name='clan_creation'),
]