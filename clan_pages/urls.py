from django.urls import path
from. import views

urlpatterns = [
    # clan pages are displayed through the index app url
    path('clan/<str:clan_name>/', views.clan_page, name='clan_page'),
    path('clan_creation/', views.clan_creation, name='clan_creation'),
    path('clan/edit/<str:clan_name>/', views.edit_clan_page, name='edit_clan_page'),
]
