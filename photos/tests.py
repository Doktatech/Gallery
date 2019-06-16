from django.test import TestCase
from .models import Uploader,Image,tags
class UploaderTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.rewel= Uploader(first_name = 'Rewel', last_name ='Kenyaa', email ='doktatech2@gmail.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.rewel,Uploader))
    def test_save_method(self):
        self.rewel.save_uploader()
        uploaders = Uploader.objects.all()
        self.assertTrue(len(uploaders) > 0)
class tagsTestClass(TestCase):
    def setUp(self):
        self.rewel= Uploader(first_name = 'Rewel', last_name ='Kenyaa', email ='doktatech2@gmail.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.rewel,tags))
class ImageTestClass(TestCase):
    
    def setUp(self):
        self.rewel= Uploader(first_name = 'Rewel', last_name ='Kenyaa', email ='doktatech2@gmail.com')
        self.rewel.save_uploader()

        self.new_tag = tags(name='Testing')
        self.new_tag.save()

        self.new_image =Image(image_name='Test Image',uploader=self.rewel,image_description='This is a simple description',image_location='Nairobi',image_category='Nature')
        self.new_image.save()
        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Uploader.objects.all().delete()
        tags.objects.all().delete()        
        Image.objects.all().delete()
    def test_photos_today(self):
        photos_today= Image.todays_photos()
        self.assertTrue(len(photos_today)>0)
   

