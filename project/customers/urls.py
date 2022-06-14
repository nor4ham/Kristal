from django.urls import path
from . import api 

urlpatterns = [
#customer/signup/
path('signup/', api.CustomerSinup , name='customer_signup'),
#customer/login/
path('login/', api.LoginCustomer , name='login_customer'),

    # GET  from rest framework class based view APIView
    path('profiles/', api.Customer_List.as_view() , name='profile'),

    #GET PUT DELETE from rest framework class based view APIView
    path('profile/<int:pk>', api.Customer_pk.as_view(), name='profile'),

]
