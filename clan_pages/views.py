from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CreateClan
from .models import Clan

# indiviual clan page
def clan_page(request, clan_name):
    clan = get_object_or_404(Clan, clan_name=clan_name)
    return render(request, 'clan_page.html', {'clan': clan, 'current_user': request.user})

# Clan creation.
def clan_creation(request):
    if request.method == "POST":
        print("Received a POST request")
        
        # Check if the user already has a clan
        if Clan.objects.filter(user=request.user).exists():
            messages.add_message(request, messages.ERROR, "ERROR, a clan is already associated with this account")
            return redirect('index')

        form = CreateClan(data=request.POST)
        if form.is_valid():
            print("Form is valid, creating clan")
            clan = form.save(commit=False)
            clan.user = request.user
            clan.save()
            messages.add_message(request, messages.SUCCESS, 'Clan created successfully')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Form is not valid')
            
    form = CreateClan()

    return render(request, 'clan_creation.html', {'clanCreation': form})

# edit clan page
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

# delete clan page
def delete_clan(request, clan_name):
    clan = get_object_or_404(Clan, clan_name=clan_name)

    # Check if the user is authorized to delete the clan
    if request.user == clan.user or request.user.is_superuser:
        clan.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'clan deleted'
        )   
        return redirect('index')