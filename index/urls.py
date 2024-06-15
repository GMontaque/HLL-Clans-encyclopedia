from django.urls import path
from . import views
from clan_pages.views import clan_page
from .views import IndexView, LoginPopupView, LogoutPopupView

urlpatterns = [
    # url path to index page
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginPopupView.as_view(), name='login_popup'),
    path('logout/', LogoutPopupView.as_view(), name='logout_popup'),
]
