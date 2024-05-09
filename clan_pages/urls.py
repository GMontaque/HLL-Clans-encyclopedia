from django.urls import path
from. import views

urlpatterns = [
    path('', views.clan_page, name='clan_page'),
]