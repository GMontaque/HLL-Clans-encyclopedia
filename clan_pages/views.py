from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CreateClan
from .models import Clan

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
    clan = get_object_or_404(Clan, clan_name=clan_name)
    
    if request.method == 'POST':
        form = CreateClan(request.POST, instance=clan)
        if form.is_valid():
            form.save()
            return redirect('clan_page', clan_name=clan.clan_name)
    else:
        form = CreateClan(instance=clan)
    
    return render(request, 'edit_clan_page.html', {'edit_clan_form': form, 'clans': clan})
