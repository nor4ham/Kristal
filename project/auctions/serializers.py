#### get data from model ---> json
from .models import   auction

from rest_framework import serializers

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = auction
        fields = '__all__'


