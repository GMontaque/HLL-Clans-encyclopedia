from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from clan_pages.models import Clan
from profiles.models import UserProfile


# displays index page with clans
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'clans'

    def get_queryset(self):
        return Clan.objects.order_by('clan_name')


class LoginPopupView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        response = login(request, *args, **kwargs)
        messages.success(request, 'Signed in successfully')
        return redirect('index')


class LogoutPopupView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        response = logout(request, *args, **kwargs)
        messages.info(request, 'Signed out successfully')
        return redirect('index')


def error_view(request):
    return render(request, '404.html')
