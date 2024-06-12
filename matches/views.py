from django.shortcuts import render, redirect
from .forms import ClamMatchForm
from clan_pages.models import Clan
from .models import Match
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def match_request(request):
    # checks if user has created a clan
    if not Clan.objects.filter(user=request.user).exists() and not request.user.is_superuser:
        messages.add_message(request, messages.ERROR,
                             'You must make a clan before you can request a game')
        return redirect('clan_creation')

    # Handle form submission
    if request.method == "POST":
        form = ClamMatchForm(data=request.POST, user=request.user)
        if form.is_valid():
            # Save the form but don't commit
            match = form.save(commit=False)
            # Set the inviter_clan based on the user context
            if not request.user.is_superuser:
                match.inviter_clan = Clan.objects.get(user=request.user)
            else:
                selected_user = request.POST.get('selected_user')
                if selected_user:
                    match.inviter_clan = Clan.objects.get(user=User.objects.get(username=selected_user))
            # Save and commit
            match.save()
            messages.add_message(request, messages.SUCCESS, 'Match request sent')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Form is not valid')
    else:
        form = ClamMatchForm(user=request.user)

    # Get the list of users for the admin dropdown
    users = User.objects.exclude(username='admin').filter(clan__isnull=False)
    return render(request, 'match_request.html', {'match_form': form, 'users': users})


# displays individual match requests
@login_required
def requested_game(request, pk):
    matches = Match.objects.filter(pk=pk)
    clan_name = "admin"
    if request.user.username != "admin":
        clan = Clan.objects.get(user=request.user.id)
        clan_name = clan.clan_name
    return render(request, 'requested_game.html', {'matches': matches,
                                                   'user_clan': clan_name})


# updates game request and redirects to notifications page
@login_required
def update_game_request_status(request, pk, is_accepted):
    # gets match by primary key value
    matches = Match.objects.filter(pk=pk).first()
    if is_accepted in ['accepted', 'rejected']:
        matches.is_accepted = is_accepted
        matches.save()
    return redirect('notifications')
