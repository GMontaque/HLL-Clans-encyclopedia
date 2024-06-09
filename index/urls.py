from django.urls import path
from . import views
from clan_pages.views import clan_page

urlpatterns = [
    # url path to index page
    path('', views.index, name='index'),
]
