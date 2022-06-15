from django.contrib import admin

from .models import  Horse as Profilehorse,Comment
admin.site.register(Profilehorse)
admin.site.register(Comment)
