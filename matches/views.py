from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ClamMatchForm
from .models import Match
from django.contrib.auth.models import User
from clan_pages.models import Clan
from django.db.models import Q
from notifications.views import get_all_notifications

# Create your views here.
def match_request(request):
    match_form = ClamMatchForm()
    return render(request, 'match_request.html',{'match_form': match_form})

def requested_game(request, pk):
    matches = Match.objects.filter(pk=pk)
    return render(request, 'requested_game.html',{'matches': matches})

def update_game_request_status(request, pk, is_accepted):
    matches = Match.objects.filter(pk=pk).first()
    if is_accepted in ['accepted', 'rejected']:
        matches.is_accepted = is_accepted
        matches.save()
    all_notifications = get_all_notifications(request.user)
    clan = Clan.objects.get(user=request.user.id)
    matches = Match.objects.filter(Q(inviter_clan_id=clan.id) | Q(invitee_clan_id=clan.id))
    
    return render(request, 'notifications.html', {
        'all_notifications': all_notifications,
        'current_user': request.user,
        'matches':matches
    })