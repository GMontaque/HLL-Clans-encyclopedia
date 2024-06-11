from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ClamMatchForm
from clan_pages.models import Clan
from .models import Match
from django.contrib.auth.models import User
from clan_pages.models import Clan
from django.db.models import Q
from notifications.views import get_all_notifications
from django.contrib import messages


# displays match request page and form
def match_request(request):
    # checks if user has created a clan
    if not Clan.objects.filter(user=request.user).exists() and not request.user.username == "admin":
        messages.add_message(request, messages.ERROR,
                                 'You must make a clan before you can request a game')
        return redirect('clan_creation')
    users = None
    if request.user.username == "admin":
        users = User.objects.all()

    # submits forms if valid and method has a value of post
    if request.method == "POST":
        form = ClamMatchForm(data=request.POST)
        if form.is_valid():
            # Saves the form but don't commit
            match = form.save(commit=False)

            # Set the inviter_clan based on the user context
            if request.user.username != "admin":
                match.inviter_clan = Clan.objects.get(user=request.user)
            else:
                selected_user = request.POST.get('selected_user')
                if selected_user:
                    match.inviter_clan = Clan.objects.get(user=User.objects.get(username=selected_user))

            # Saves and commits
            match.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Match request sent')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Form is not valid')
    # removes admin from drop down list
    users = User.objects.exclude(username='admin').filter(clan__isnull=False)
    # match request form
    match_form = ClamMatchForm()
    return render(request, 'match_request.html', {'match_form': match_form,
                                                  'users': users})


# displays individual match requests
def requested_game(request, pk):
    matches = Match.objects.filter(pk=pk)
    clan_name = "admin"
    if request.user.username != "admin":
        clan = Clan.objects.get(user=request.user.id)
        clan_name = clan.clan_name
    return render(request, 'requested_game.html', {'matches': matches,
                                                   'user_clan': clan_name})


# updates game request and redirects to notifications page
def update_game_request_status(request, pk, is_accepted):
    # gets match by primary key value
    matches = Match.objects.filter(pk=pk).first()
    if is_accepted in ['accepted', 'rejected']:
        matches.is_accepted = is_accepted
        matches.save()
    return redirect('notifications')
