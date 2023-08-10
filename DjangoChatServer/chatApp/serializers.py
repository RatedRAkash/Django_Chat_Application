from rest_framework import serializers

from registerApp.serializers import UserRelationToOtherModelSerializer
from .models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    # eita dewa mane... `Message` model er moddhe jei `user` field ase... sheita ke jokon JSON ee Pathabo FRONTEND er kase... jano
    # sheita `user` er USER model er Data uthai niye ashe
    user = UserRelationToOtherModelSerializer()
    class Meta:
        model = Message
        fields = '__all__'