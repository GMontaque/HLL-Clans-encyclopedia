from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateClan
from .models import Clan
from django.contrib import messages


# Create your views here.
# clan indiviual page view
def clan_page(request, clan_name):
    clan = get_object_or_404(Clan, clan_name=clan_name)
    return render(request, 'clan_page.html', {'clan': clan})

# Clan creation.
def clan_creation(request):
    if request.method == "POST":
        print("Received a POST request")
        form = CreateClan(data=request.POST)
        if form.is_valid():
            print("sent ==============")
            comment = form.save(commit=False)
            comment.user = request.user
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'clan created'
            )   
    form = CreateClan()
    return render(request, 'clan_creation.html', {'clanCreation': form}) 


def edit_clan_page(request, clan_name):
    pass
