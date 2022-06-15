from .models import auction 
from .serializers import AuctionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from kristal.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

 
# Horse_List Class based views
# List and Create == GET and POST
class Auction_List(APIView):
    """This endpoint  List and Create  of the Horse from the database"""  
    def get(self, request):
        profiles = auction.objects.all()
        serializer = AuctionSerializer(profiles, many = True)
        return Response(serializer.data)
    @permission_classes([IsAuthenticated])
    def post(self, request):
     user:User = request.user
     if user.is_authenticated and user.has_perm("horses.add_horse"):
        serializer = AuctionSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status .HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_40
        )
     return Response({"msg" : "login plz or u dont have permissions"})

#4.2 GET PUT DELETE cloass based views -- pk 
class  auction_pk(APIView):

    def get_object(self, pk):
        try:
            return auction.objects.get(pk=pk)
        except auction.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = AuctionSerializer(profile)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
     user:User = request.user
     if user.is_authenticated and user.has_perm("horses.change_horse"):      
        profile = self.get_object(pk)
        serializer = AuctionSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     return Response({"msg" : "login plz or u dont have permissions"})

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
     user:User = request.user
     if user.is_authenticated and  user.has_perm("horses.delete_horse"):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     return Response({"msg" : "login plz or u dont have permissions  "})


 
   