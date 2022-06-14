from django.urls import path
from . import api 

urlpatterns = [

#seller/signup/
path('signup/', api.SellerSinup , name='seller_signup'),
#seller/login/
path('login/', api.LoginSeller , name='login_seller'),


    # GET  from rest framework class based view APIView
    path('profiles/', api.Seller_List.as_view() , name='profile'),

    #GET PUT DELETE from rest framework class based view APIView
    path('profile/<int:pk>', api.Seller_pk.as_view(), name='profile'),

]

