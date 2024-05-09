from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.
def clan_page(request):
    return render(request, 'clan_page.html')
    