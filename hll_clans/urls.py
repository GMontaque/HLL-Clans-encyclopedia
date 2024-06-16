"""
URL configuration for hll_clans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, path
from django.conf.urls import handler404
from index.views import error_view

hander404 = error_view


urlpatterns = [
    path('', include('index.urls'), name='index'),
    # goes to the clan page and clan creation html
    path('', include('clan_pages.urls'), name='clans'),
    path('match_request/', include('matches.urls'), name='matchs'),
    path(
        'notifications/',
        include('notifications.urls'),
        name='notifications'
    ),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
]
