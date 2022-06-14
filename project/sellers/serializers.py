#### get data from model ---> json
from .models import ProfileSeller
from kristal.models import User

from rest_framework import serializers

class ProfileSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSeller
        fields = '__all__'



class SellerSinupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']