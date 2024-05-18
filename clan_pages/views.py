from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateClan
from .models import Clan


# Create your views here.
# clan indiviual page view
def clan_page(request, clan_name):
    clan = get_object_or_404(Clan, clan_name=clan_name)
    return render(request, 'clan_page.html', {'clan': clan})

# Clan creation.
def clan_creation(request):
    form = CreateClan()
    return render(request, 'clan_creation.html', {'form': form}) 