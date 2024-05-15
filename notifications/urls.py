from django.urls import path
from. import views

urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('admin_ticket/', views.admin_notifications, name='admin_ticket'),
]