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

urlpatterns = [
    path('', include('index.urls'), name='index'),
    path('clan_page', include('clan_pages.urls'), name='clans'),
    path('clan_creation/', include('clan_creation.urls'), name='clan_creation'),
    path('match_request/', include('matches.urls'), name='matchs'),
    path('notifications/', include('notifications.urls'), name='notifications'),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
]

