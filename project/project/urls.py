from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('kristal/', include('kristal.urls')),
    path('customer/', include('customers.urls')),
    path('seller/', include('sellers.urls')),
    path('horses/', include('horses.urls')),
     path('', include('auctions.urls')),


    
#    path('accounts/', include('django.contrib.auth.urls')),




]
