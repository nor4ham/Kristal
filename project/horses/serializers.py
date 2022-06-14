#### get data from model ---> json
from .models import Profileseller,Comment

from rest_framework import serializers

class ProfileHorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profileseller
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'