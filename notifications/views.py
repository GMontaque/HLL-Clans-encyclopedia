from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Notification
from .forms import CreateNotification
from django.contrib import messages


# Create your views here.
def notifications(request):
    if request.user.is_authenticated:
        temp = Notification.objects.filter(receiver=request.user)
    else:
        temp = Notification.objects.none() 
    return render(request, 'notifications.html', {'notifications':temp})

def update_notification_status(request, pk, status):
    notification = get_object_or_404(Notification, pk=pk)
    if status in ['completed', 'rejected']:
        notification.status = status
        notification.save()
    if request.user.is_authenticated:
        temp = Notification.objects.filter(receiver=request.user)
    return render(request, 'notifications.html', {'notifications':temp})

def admin_notifications(request):
    if request.method == "POST":
        print("Received a POST request")
        form = CreateNotification(data=request.POST)
        if form.is_valid():
            print("sent ==============")
            form.save(commit=True)
            messages.add_message(
                request, messages.SUCCESS,
                'notification sent'
            )
            if request.user.is_authenticated:
                temp = Notification.objects.filter(receiver=request.user)
            else:
                temp = Notification.objects.none() 
            return render(request, 'notifications.html', {'notifications':temp})  
    form = CreateNotification()
    return render(request, 'admin_ticket.html',{'createNotification': form})

def show_notification(request, notification_id):
    indiv_notification = get_object_or_404(Notification, pk=notification_id)
    return render(request, 'indiv_notification.html', {'notification': indiv_notification})

