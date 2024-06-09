from django.urls import path
from . import views

urlpatterns = [
    # displays clan page
    path('clan/<str:clan_name>/', views.clan_page, name='clan_page'),
    # creates clan page
    path('clan_creation/', views.clan_creation, name='clan_creation'),
    # edit clan page
    path('clan/edit/<str:clan_name>/', views.edit_clan_page,
         name='edit_clan_page'),
    # deletes clan page
    path('clan/delete/<str:clan_name>/', views.delete_clan,
         name='delete_clan'),
]
