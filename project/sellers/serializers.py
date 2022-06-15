#### get data from model ---> json
from .models import Seller as Profileseller
from kristal.models import User

from rest_framework import serializers

class ProfileSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profileseller
        fields = '__all__'



class SellerSinupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']