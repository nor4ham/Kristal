#### get data from model ---> json
from .models import ProfileCustomer
from kristal.models import User

from rest_framework import serializers

class ProfileCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomer
        fields = '__all__'



class CustomerSinupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']