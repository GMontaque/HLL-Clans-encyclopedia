from django.urls import path
from. import views

urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('admin_ticket/', views.admin_notifications, name='admin_ticket'),
    path('notification/<int:notification_id>/', views.show_notification, name='individual_notification'),
    path('notification/<int:pk>/update/<str:status>/', views.update_notification_status, name='update_notification_status')
]