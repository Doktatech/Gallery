from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt 
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to  my photo gallery')

def photos_of_day(request):
    date = dt.date.today()
    day =convert_dates(date)
    html= f''''
        <html>
            <body>
            <h1> Photos of {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)
def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number=dt.date.weekday(dates)
    days= ["Moday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day =days[day_number]
    return day 
def past_days_photos(request):
    # Function for getting archived photos 