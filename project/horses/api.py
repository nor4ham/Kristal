from .models import ProfileHorse,Comment 
from .serializers import ProfileHorseSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from kristal.models import User
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

 
# Horse_List Class based views
#4.1 List and Create == GET and POST
class Horse_List(APIView):
    """This endpoint  List and Create  of the Horse from the database"""  
    def get(self, request):
        profiles = ProfileHorse.objects.all()
        serializer = ProfileHorseSerializer(profiles, many = True)
        return Response(serializer.data)
    #@authentication_classes([JWTAuthentication])   
    def post(self, request):
     user:User = request.user
     if user.is_authenticated:
        serializer = ProfileHorseSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_40
        )
     return Response({"msg" : "login plz"})

#4.2 GET PUT DELETE cloass based views -- pk 
class  Horse_pk(APIView):

    def get_object(self, pk):
        try:
            return ProfileHorse.objects.get(pk=pk)
        except ProfileHorse.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileHorseSerializer(profile)
        return Response(serializer.data)
    @authentication_classes([JWTAuthentication])   
    def put(self, request, pk):
     user:User = request.user
     if user.is_authenticated:        
        profile = self.get_object(pk)
        serializer = ProfileHorseSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     return Response({"msg" : "login plz"})

    @authentication_classes([JWTAuthentication])
    def delete(self, request, pk):
     user:User = request.user
     if user.is_authenticated:   
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     return Response({"msg" : "login plz"})


 
   










# Comment Class based views
#4.1 List and Create == GET and POST


class Comment_List(APIView):
    """This endpoint  List and Create  of the Comment from the database"""  
       
    def get(self, request):
        profiles = Comment.objects.all()
        serializer = CommentSerializer(profiles, many = True)
        return Response(serializer.data)
    @authentication_classes([JWTAuthentication])
    def post(self, request):
     user:User = request.user
     if user.is_authenticated:
        serializer = CommentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_40
        )
     return Response({"msg" : "login plz"})

#4.2 GET PUT DELETE cloass based views -- pk 
class  Comment_pk(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = CommentSerializer(profile)
        return Response(serializer.data)
    @authentication_classes([JWTAuthentication])     
    def put(self, request, pk):
     user:User = request.user
     if user.is_authenticated:   
        profile = self.get_object(pk)
        serializer = CommentSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     return Response({"msg" : "login plz"})
    @authentication_classes([JWTAuthentication])    
    def delete(self, request, pk):
     user:User = request.user
     if user.is_authenticated: 
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     return Response({"msg" : "login plz"})    