from django.urls import path
from . import api 

urlpatterns = [
#horses
    path('', api.Horse_List.as_view() , name='profiles'),
    path('add_horse/', api.Horse_List.as_view() , name='add_horse'),

    #GET PUT DELETE from rest framework class based view APIView
    path('horse/<int:pk>', api.Horse_pk.as_view(), name='profile'),
    path('update_horse/<int:pk>', api.Horse_pk.as_view(), name='update_horse'),
    path('delete_horse/<int:pk>', api.Horse_pk.as_view(), name='update_horse'),
#horses
    path('comments/', api.Comment_List.as_view() , name='comments'),
    path('add_comment/', api.Comment_List.as_view() , name='add_comment'),

    #GET PUT DELETE from rest framework class based view APIView
    path('comment/<int:pk>', api.Comment_pk.as_view(), name='comment'),
    path('update_comment/<int:pk>', api.Comment_pk.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>', api.Comment_pk.as_view(), name='delete_comment'),

]


