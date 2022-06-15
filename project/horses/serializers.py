#### get data from model ---> json
from .models import  Horse as Profilehorse,Comment

from rest_framework import serializers

class ProfileHorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilehorse
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'