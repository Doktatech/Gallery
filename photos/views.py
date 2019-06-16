from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt 
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
     
    return render(request, 'all-photos/today-photos.html',{"date":date,})

def past_days_photos(request,past_date):
    # Function for getting archived photos 
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 ERROR
        raise Http404()
        assert False
    if  date == dt.date.today():
        return redirect(photos_of_day)
  
    
    return render(request, 'all-photos/past-photos.html',{"date":date,})
