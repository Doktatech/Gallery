from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt 
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    day =convert_dates(date)    
    return HttpResponse(html)
def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number=dt.date.weekday(dates)
    days= ["Moday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day =days[day_number]
    return day 
def past_days_photos(request,past_date):
    # Function for getting archived photos 
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 ERROR
        raise Http404
    day =convert_dates(date)
    
    return HttpResponse(html)
