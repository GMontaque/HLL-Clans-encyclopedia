from django.urls import path
from. import views

urlpatterns = [
    # displays notification page
    path('', views.notifications, name='notifications'),
    # displays admin ticket creation form
    path('admin_ticket/', views.admin_notifications, name='admin_ticket'),
    # displays individual notification
    path('notification/<int:notification_id>/', views.show_notification, name='individual_notification'),
    # displays page to edit individual notification
    path('notification/<int:pk>/update/<str:status>/', views.update_notification_status, name='update_notification_status')
]