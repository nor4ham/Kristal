from .models import Profilehorse,Comment 
from .serializers import ProfileHorseSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from kristal.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

 
# Horse_List Class based views
# List and Create == GET and POST
class Horse_List(APIView):
    """This endpoint  List and Create  of the Horse from the database"""  
    def get(self, request):
        profiles = Profilehorse.objects.all()
        serializer = ProfileHorseSerializer(profiles, many = True)
        return Response(serializer.data)
    @permission_classes([IsAuthenticated])
    def post(self, request):
     user:User = request.user
     if user.is_authenticated and user.has_perm("horses.add_profilehorse"):
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
     return Response({"msg" : "login plz or u dont have permissions"})

#4.2 GET PUT DELETE cloass based views -- pk 
class  Horse_pk(APIView):

    def get_object(self, pk):
        try:
            return Profilehorse.objects.get(pk=pk)
        except Profilehorse.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileHorseSerializer(profile)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
     user:User = request.user
     if user.is_authenticated and user.has_perm("horses.change_profilehorse"):      
        profile = self.get_object(pk)
        serializer = ProfileHorseSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     return Response({"msg" : "login plz or u dont have permissions"})

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
     user:User = request.user
     if user.is_authenticated and  user.has_perm("horses.delete_profilehorse"):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     return Response({"msg" : "login plz or u dont have permissions  "})


 
   










# Comment Class based views
#4.1 List and Create == GET and POST


class Comment_List(APIView):
    """This endpoint  List and Create  of the Comment from the database"""  
       
    def get(self, request):
        profiles = Comment.objects.all()
        serializer = CommentSerializer(profiles, many = True)
        return Response(serializer.data)
    @permission_classes([IsAuthenticated])
    def post(self, request):
     user:User = request.user
     if user.is_authenticated and user.has_perm("horses.add_comment"):
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
     return Response({"msg" : "login plz or u dont have permissions"})

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

    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
     user:User = request.user
     if user.is_authenticatedand and user.has_perm("horses.change_comment"):   
        profile = self.get_object(pk)
        serializer = CommentSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     return Response({"msg" : "login plz or u dont have permissions"})

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
     user:User = request.user
     if user.is_authenticated and  user.has_perm("horses.delete_comment"):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     return Response({"msg" : "login plz or u dont have permissions"})    