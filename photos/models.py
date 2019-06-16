from django.db import models
# Create your models here.
class Uploader(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']
    
    # try:
    #     uploader = Uploader.objects.get(email = 'example@gmail.com')
    #     print('Uploader found')
    # except DoesNotExist:
    #     print('Uploader was not found')
class tags(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name
class Image(models.Model):
    image_name= models.CharField(max_length=50)
    uploader = models.ForeignKey(Uploader)
    photo_image =models.ImageField(upload_to='photos/')
    tags = models.ManyToManyField(tags)
    image_description = models.TextField()    
    upload_date = models.DateField(auto_now_add=True)
    image_location= models.CharField(max_length=60)
    image_category=models.CharField(max_length=50)


