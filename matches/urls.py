from django.urls import path
from. import views

urlpatterns = [
    path('', views.match_request, name='match_request'),
    path('requested_game/', views.requested_game, name='requested_game'),
]