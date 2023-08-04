from rest_framework import serializers
from .models import Room, Message

class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = '__all__'