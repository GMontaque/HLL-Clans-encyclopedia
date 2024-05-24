from django.urls import path
from. import views

urlpatterns = [
    path('', views.match_request, name='match_request'),
    path('requested_game/<int:pk>', views.requested_game, name='requested_game'),
    path('requested_game/<int:pk>/<str:is_accepted>', views.update_game_request_status, name='update_game_request'),
]