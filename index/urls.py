from django.urls import path
from. import views
from clan_pages.views import clan_page

urlpatterns = [
    path('', views.index, name='index'),
    # displays the individual clan page
    
]