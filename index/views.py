from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from clan_pages.models import Clan
from profiles.models import UserProfile

def index(request):
    clans = Clan.objects.all()
    return render(request, 'index.html', {'clans': clans})
  