from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ClamMatchForm
from .models import Match
from django.contrib.auth.models import User
from clan_pages.models import Clan
from django.db.models import Q
from notifications.views import get_all_notifications
from django.contrib import messages

# displays match request page and form
def match_request(request):
    users = None
    if request.user.username == "admin":
        users = User.objects.all()
    # submits forms if valid and method has a value of post
    if request.method == "POST":
        print("Received a POST request")
        
        form = ClamMatchForm(data=request.POST)
        if form.is_valid():
            if request.user.username != "admin":
                clan.inviter_clan = User.objects.get(username=request.POST.get('selected_user')) if request.POST.get('selected_user') else request.user
            clan = form.save(commit=False)
            clan.save()
            messages.add_message(request, messages.SUCCESS, 'match request sent')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Form is not valid')
    # match request form
    match_form = ClamMatchForm()
    return render(request, 'match_request.html',{'match_form': match_form, 'users':users})

# displays individual match requests
def requested_game(request, pk):
    matches = Match.objects.filter(pk=pk)
    clan = Clan.objects.get(user=request.user.id)
    return render(request, 'requested_game.html',{'matches': matches,'user_clan': clan.clan_name })

# updates game request and redirects to notifications page
def update_game_request_status(request, pk, is_accepted):
    # gets match by primary key value
    matches = Match.objects.filter(pk=pk).first()
    if is_accepted in ['accepted', 'rejected']:
        matches.is_accepted = is_accepted
        matches.save()
    return redirect('notifications')