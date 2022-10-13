from rest_framework.serializers import ModelSerializer
from base.models import Rooms ,Message
from django.contrib.auth.models import User

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
        
        
        
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'