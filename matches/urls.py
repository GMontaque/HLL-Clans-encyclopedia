from django.urls import path
from . import views

urlpatterns = [
    # displays game request form
    path('', views.match_request, name='match_request'),
    # displays individual game requests
    path('requested_game/<int:pk>', views.requested_game,
         name='requested_game'),
    # updates game request status
    path('requested_game/<int:pk>/<str:is_accepted>',
         views.update_game_request_status, name='update_game_request'),
]
