from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from clan_pages.models import Clan
from profiles.models import UserProfile
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect


# displays index page with clans
def index(request):
    clans = Clan.objects.order_by('clan_name')
    return render(request, 'index.html', {'clans': clans})


# displays logged in message
def login_popup(request, *args, **kwargs):
    response = login(request, *args, **kwargs)
    messages.success(request, 'Signed in successfully')
    return redirect('index.html')


# displays logged out message
def logout_popup(request, *args, **kwargs):
    response = logout(request, *args, **kwargs)
    messages.info(request, 'Signed out successfully')
    return redirect('index.html')


def error_view(request):
    return render(request, '404.html')
