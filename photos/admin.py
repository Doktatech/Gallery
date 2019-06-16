from django.contrib import admin
from .models import Uploader,Image,tags
class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Uploader)
admin.site.register(Image)
admin.site.register(tags)

# Register your models here.
