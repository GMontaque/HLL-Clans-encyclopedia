from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Notification
from .forms import CreateNotification
from django.contrib import messages
from clan_pages.models import Clan
from django.db.models import Q
from matches.models import Match
from django.contrib.auth.models import User

# Helper function to get all notifications for the authenticated user
def get_all_notifications(user):
    if user.is_authenticated:
        return Notification.objects.filter(Q(receiver=user) | Q(issuer=user))
    return Notification.objects.none()

# View to show notifications
def notifications(request):
    all_notifications = get_all_notifications(request.user)
    clan = Clan.objects.get(user=request.user.id)
    admin_user = User.objects.filter(is_superuser=True).first()
    if request.user == admin_user:
        matches = Match.objects.all()
    else:
        matches = Match.objects.filter(Q(inviter_clan_id=clan.id) | Q(invitee_clan_id=clan.id))
    return render(request, 'notifications.html', {
        'all_notifications': all_notifications,
        'current_user': request.user,
        'matches':matches,
        'user_clan': clan.clan_name 
    })

# View to update the status of a notification
def update_notification_status(request, pk, status):
    notification = get_object_or_404(Notification, pk=pk)
    if status in ['completed', 'rejected']:
        notification.status = status
        notification.save()
    
    all_notifications = get_all_notifications(request.user)
    return render(request, 'notifications.html', {
        'all_notifications': all_notifications,
        'current_user': request.user
    })

# View for admin notifications
def admin_notifications(request):
    if request.method == "POST":
        form = CreateNotification(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(
                request, messages.SUCCESS,
                'Notification sent'
            )
            all_notifications = get_all_notifications(request.user)
            return render(request, 'notifications.html', {
                'all_notifications': all_notifications,
                'current_user': request.user
            })  
    form = CreateNotification()

    return render(request, 'admin_ticket.html', {'createNotification': form, 'issuer': request.user})

# View to show individual notification details
def show_notification(request, notification_id):
    indiv_notification = get_object_or_404(Notification, pk=notification_id)
    return render(request, 'indiv_notification.html', {'notification': indiv_notification})


