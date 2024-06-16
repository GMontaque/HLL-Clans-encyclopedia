from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Notification
from .forms import CreateNotification
from django.contrib import messages
from clan_pages.models import Clan
from django.db.models import Q
from matches.models import Match
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# function gets all notifications for the authorized user
def get_all_notifications(user):
    if user.is_authenticated:
        return Notification.objects.filter(
            Q(receiver=user) | Q(issuer=user)
            ).order_by('-create_at')
    return Notification.objects.none()


# displays notification page and data
@login_required
def notifications(request):
    # gets notifications based on user
    all_notifications = get_all_notifications(request.user)
    paginator = Paginator(all_notifications, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # gets admin user
    admin_user = User.objects.filter(is_superuser=True).first()

    if request.user == admin_user:
        matches = Match.objects.all()
        clan_name = "Admin Clan"  # sets clan name to admin for the admin user
    else:
        # gets clan page based on user id
        try:
            clan = Clan.objects.get(user=request.user.id)
            matches = Match.objects.filter(
                Q(inviter_clan_id=clan.id) | Q(invitee_clan_id=clan.id)
                )
            clan_name = clan.clan_name
        except Clan.DoesNotExist:
            clan_name = "non-clan-rep"
            matches = Match.objects.none()

    return render(request, 'notifications.html', {
        'all_notifications': page_obj,
        'current_user': request.user,
        'matches': matches,
        'user_clan': clan_name
    })


# updates status of a notification
@login_required
def update_notification_status(request, pk, status):
    # gets individual notification by primary key
    notification = get_object_or_404(Notification, pk=pk)
    # checks value of status that has been passed
    if status in ['completed', 'in-progress', 'rejected']:
        notification.status = status
        notification.save()
    matches = Match.objects.all()
    all_notifications = get_all_notifications(request.user)
    return render(request, 'notifications.html', {
        'all_notifications': all_notifications,
        'current_user': request.user,
        'matches': matches,
    })


# displays admin notification form
@login_required
def admin_notifications(request):
    # gets admin user
    admin_user = User.objects.filter(is_superuser=True).first()
    # gets clan page based on user id
    # clan = Clan.objects.get(user=request.user.id)
    try:
        clan = Clan.objects.get(user=request.user.id)
    except Clan.DoesNotExist:
        clan = "non-clan-rep"

    if request.method == "POST":
        form = CreateNotification(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            # auto completes forms fields not shown to member
            ticket.issuer = request.user
            ticket.receiver = admin_user
            ticket.clan = clan
            ticket.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Notification sent'
            )
            return redirect('notifications')
    # notification form
    form = CreateNotification()
    return render(request, 'admin_ticket.html', {'createNotification': form,
                                                 'issuer': request.user})


# displays individual notification
@login_required
def show_notification(request, notification_id):
    indiv_notification = get_object_or_404(Notification, pk=notification_id)
    return render(request, 'indiv_notification.html',
                  {'notification': indiv_notification})
