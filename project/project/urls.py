
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
        path('', include('accounts.urls')),
        path('', include('horses.urls')),
        path('', include('admins.urls')),
        path('', include('customers.urls')),
        path('', include('sellers.urls')),
        

]

