from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Search, User
from django.core.urlresolvers import reverse
import datetime


def index(request):
    return render(request, 'Negot/index.html')

def about(request):
    return render(request, 'Negot/about.html')

def results(request):
    return render(request, 'Negot/results.html')

def search(request):
    search = Search()
    try:
        search.checkin_date = datetime.datetime.strptime(request.POST['check-in'], '%b %d, %Y').strftime('%Y-%m-%d')
        search.chechout_date = datetime.datetime.strptime(request.POST['check-out'], '%b %d, %Y').strftime('%Y-%m-%d')
        search.destination = request.POST.get('destination', 'NYC')
    except (KeyError, Search.DoesNotExist):
        # Redisplay the index form with error Infomation.
        return render(request, 'Negot/index.html')
    else:
        search.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'Negot/results.html')