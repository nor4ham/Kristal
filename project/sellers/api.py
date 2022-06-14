from .models import Profileseller
from .serializers import ProfileSellerSerializer,SellerSinupSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from kristal.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import Group

from rest_framework.views import APIView
from django.http import Http404


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Seller_List Class based views
#4.1 List and Create == GET and POST
class Seller_List(APIView):
    """This endpoint  List  of the sellers from the database"""  
       
    def get(self, request):
        profiles = Profileseller.objects.all()
        serializer = ProfileSellerSerializer(profiles, many = True)
        return Response(serializer.data)
      

#4.2 GET PUT DELETE cloass based views -- pk 
class  Seller_pk(APIView):

    def get_object(self, pk):
        try:
            return Profileseller.objects.get(pk=pk)
        except Profileseller.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSellerSerializer(profile)
        return Response(serializer.data)
    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
      user:User = request.user
      if user.is_authenticated and  user.has_perm("sellers.change_profileseller"):    
        profile = self.get_object(pk)
        serializer = ProfileSellerSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response({"msg" : "login plz or u dont have permissions"})

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
     user:User = request.user
     if user.is_authenticated and  user.has_perm("sellers.delete_profileseller"):  
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     return Response({"msg" : "login plz or u dont have permissions"})

@api_view(['POST'])
def SellerSinup(request : Request):
    
    user_serializer  = SellerSinupSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.is_seller = True
        new_user.save()
        Profileseller.objects.create(user=new_user)
        my_group = Group.objects.get(name='sellers')
        my_group.user_set.add(new_user)
        return Response({"msg" : "created user successfuly"})
    else:
        print(user_serializer.errors)
        return Response({"msg" : "Couldn't create user"}, status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def LoginSeller(request : Request):

    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            #create the token , then give the token to the user in the response
            token = AccessToken.for_user(user)
            responseData = {
                "msg" : "Your token is ready",
                "token" : str(token)
            }
            return Response(responseData)


    return Response({"msg" : "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)
