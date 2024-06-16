from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CreateClan
from .models import Clan
from matches.models import Match
from django.db.models import Q
from index.views import error_view
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# displays individual clan page
def clan_page(request, clan_name):
    try:
        clan = Clan.objects.get(clan_name=clan_name)
        matches = Match.objects.filter(
            (Q(inviter_clan_id=clan.id) |
             Q(invitee_clan_id=clan.id)) &
            Q(is_accepted="accepted")
        )
    except Clan.DoesNotExist:
        return error_view(request)
    return render(request, 'clan_page.html', {
        'clan': clan,
        'current_user': request.user,
        'matches': matches
    })


# creates Clan page
@login_required
def clan_creation(request):
    users = None
    if request.user.username == "admin":
        users = "admin"
    # checks for a post value from the method on the form
    if request.method == "POST":
        # form data to be passed to database
        data = {
            'clan_name': request.POST.get('clan_name'),
            'content': request.POST.get('content'),
            'image_url': request.FILES.get('image_url'),
            'discord_url': request.POST.get('discord_url'),
            'website_url': request.POST.get('website_url')
        }
        # checks if user is admin or clan rep
        user = (User.objects.get(username=request.POST.get('selected_user'))
                if request.POST.get('selected_user')
                else request.user)
        clan_name_lower = data["clan_name"].lower()
        # Check if the user already has a clan
        if Clan.objects.filter(user=user).exists():
            messages.add_message(request, messages.ERROR,
                                 "ERROR, a clan is already "
                                 "associated with this account")
            return redirect('index')
        elif Clan.objects.filter(clan_name__iexact=clan_name_lower).exists():
            messages.add_message(request, messages.ERROR,
                                 "ERROR, a clan with that name "
                                 "already exists.")
            return redirect('clan_creation')

        form = CreateClan(request.POST, request.FILES)
        # saves the newly created form and redirects to home page(index)
        if form.is_valid():
            clan = form.save(commit=False)
            clan.user = user
            clan.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Clan created successfully')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Form is not valid')
    # removes admin from dropdown list
    user_accounts = User.objects.exclude(username='admin')
    form = CreateClan()
    # displays clan creation page and form
    return render(request, 'clan_creation.html', {
        'clanCreation': form,
        'users': users,
        'user_accounts': user_accounts
    })


# edits clan page
@login_required
def edit_clan_page(request, clan_name):
    clan = get_object_or_404(Clan, clan_name=clan_name)

    if request.method == "POST":
        form = CreateClan(request.POST, request.FILES, instance=clan)
        if form.is_valid() and (
            request.user == clan.user or request.user.is_superuser
        ):
            clan = form.save(commit=False)
            # checks for a new image
            if 'image_url' in request.FILES:  # checks if new image is uploaded
                clan.image_url = request.FILES['image_url']
            clan.save()
            messages.add_message(request, messages.SUCCESS, 'Clan Updated')
            return redirect('clan_page', clan_name=clan.clan_name)
        else:
            messages.add_message(request, messages.ERROR,
                                 'You do not have permission to'
                                 'update this clan page')
            return redirect('index')
    else:
        form = CreateClan(instance=clan)

    return render(request, 'edit_clan_page.html', {
        'edit_clan_form': form,
        'clans': clan
    })


# deletes clan page
@login_required
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
