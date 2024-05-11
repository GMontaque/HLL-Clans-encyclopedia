from django.urls import path
from. import views

urlpatterns = [
    path('', views.clan_page, name='clan_page'),
    path('creation/', views.clan_creation, name='clan_creation'),
]
