from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ClamMatchForm

# Create your views here.
def match_request(request):
    match_form = ClamMatchForm()
    return render(request, 'match_request.html',{'match_form': match_form})