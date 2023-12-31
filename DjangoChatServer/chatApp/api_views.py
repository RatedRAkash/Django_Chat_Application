from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse, JsonResponse

from django.conf import settings
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

class AllRoomsApiView(APIView):
    authentication_classes = [JWTAuthentication]  # JwtAuthentication is Needed
    permission_classes = [IsAuthenticated]  # Allow access to all users, authenticated or not

    api_name = "api/rooms"

    def get(self, request):
        rooms = Room.objects.all()
        room_serializer = RoomSerializer(rooms, many=True)
        return Response(room_serializer.data, content_type="application/json")
        # return JsonResponse(room_serialized.data, safe=False) #Above Two Lines can be written just by Using JsonResponse

    def post(self, request):
        room_serialized = RoomSerializer(data=request.data)
        if room_serialized.is_valid():
            room_serialized.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(room_serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesOfARoom(APIView):
    authentication_classes = [JWTAuthentication]  # JwtAuthentication is Needed
    permission_classes = [IsAuthenticated]  # Allow access to all users, authenticated or not

    api_name = "api/message_of_a_room"

    def get(self, request, room_slug):
        room = Room.objects.get(slug=room_slug)
        messages = room.messages.all()
        msg_serializer = MessageSerializer(messages, many=True)
        return Response(msg_serializer.data, content_type="application/json")

    # Don't Need POST Method as User will `post` messages through WEBSOCKET Api
    def post(self, request):
        pass