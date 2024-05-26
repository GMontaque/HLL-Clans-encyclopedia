from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CreateClan
from .models import Clan
from matches.models import Match
from django.db.models import Q

# displays indiviual clan page
def clan_page(request, clan_name):
    clan = Clan.objects.get(clan_name=clan_name)
    matches = Match.objects.filter((Q(inviter_clan_id=clan.id) | Q(invitee_clan_id=clan.id)) & Q(is_accepted="accepted"))
    return render(request, 'clan_page.html', {'clan': clan, 'current_user': request.user, 'matches':matches})

# creates Clan page
def clan_creation(request):
    # checks for a post value from the method on the form
    if request.method == "POST":
        print("Received a POST request")
        
        # Check if the user already has a clan
        if Clan.objects.filter(user=request.user).exists():
            messages.add_message(request, messages.ERROR, "ERROR, a clan is already associated with this account")
            return redirect('index')

        form = CreateClan(data=request.POST)
        # saves the newly created form and redirects to home page(index)
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
    # displays clan creation page and form
    return render(request, 'clan_creation.html', {'clanCreation': form})

# edits clan page
def edit_clan_page(request, clan_name):
    # gets specific clan based on clan name
    clan = get_object_or_404(Clan, clan_name=clan_name)
    # checks for a post value from the method on the form
    # saves edited form
    if request.method == 'POST':
        form = CreateClan(request.POST, instance=clan)
        if form.is_valid():
            form.save()
            return redirect('clan_page', clan_name=clan.clan_name)
    else:
        form = CreateClan(instance=clan)
    # displays the edit clan page and form
    return render(request, 'edit_clan_page.html', {'edit_clan_form': form, 'clans': clan})

# deletes clan page
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