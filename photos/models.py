import datetime as dt
from django.db import models
# Create your models here.
class Uploader(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    def __str__(self):
        return self.first_name
    def save_uploader(self):
        self.save()
    class Meta:
        ordering = ['first_name']    
    
class tags(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name
class Image(models.Model):
    class Meta:
        ordering = ['image_location']
    image_name= models.CharField(max_length=50)
    uploader = models.ForeignKey(Uploader)
    photo_image =models.ImageField(upload_to='pictures/')
    tags = models.ManyToManyField(tags)
    image_description = models.TextField()    
    upload_date = models.DateTimeField(auto_now_add=True)
    image_location= models.CharField(max_length=60)
    image_category=models.CharField(max_length=50)
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(upload_date__date = today)
        return photos
    @classmethod
    def days_photos(cls,date):
        # today = dt.date.today()
        photos = cls.objects.filter(upload_date__date = date)
        return photos
    @classmethod 
    def all_photos(cls):
        photos = cls.objects.all()
        return photos

        
    @classmethod
    def search_by_image_category(cls, search_term):
        photos= cls.objects.filter(image_category__icontains=search_term)
        return photos