#### get data from model ---> json
from .models import ProfileCustomer
from rest_framework import serializers

class ProfileCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomer
        fields = '__all__'

