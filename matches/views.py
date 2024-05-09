from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.
def match_request(request):
    return render(request, 'match_request.html')