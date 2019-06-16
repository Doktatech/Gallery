from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt 
from .models import Image
# # Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    photos = Image.todays_photos()
     
    return render(request, 'all-photos/today-photos.html',{"date":date,"photos":photos})

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
        photos = Image.days_photos(date)
  
    
    return render(request, 'all-photos/past-photos.html',{"date":date,"photos":photos})
def search_results(request):

        if 'photo' in request.GET and request.GET["photo"]:
            search_term = request.GET.get("photo")
            searched_photo = Image.search_by_image_category(search_term)
            message = f"{search_term}"

            return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photo})

        else:
            message = "You haven't searched for any photo"
            return render(request, 'all-photos/search.html',{"message":message})
def single_photo(request,photo_id):
    try:
        photo = Image.objects.get(id=photo_id)  
    except DoesNotExist:
        raise Http404()
        
    return render(request,"all-photos/photo.html",{"photo":photo})

