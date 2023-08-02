from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import *

# Create your views here.
def lobby(request):
    return render(request, 'chatApp/lobby.html')


@method_decorator(login_required, name='dispatch')
class AllRoomsView(View):
    def get(self, request):
        all_rooms = Room.objects.all()
        return render(request, 'chatApp/all_rooms.html', {'rooms':all_rooms})

@method_decorator(login_required, name='dispatch')
class SingleRoomView(View):
    def get(self, request, slug):
        single_room = Room.objects.get(slug=slug)
        messages = Message.objects.filter(room=single_room)[0:24] #first 24 ta Message dekhabo amra

        return render(request, 'chatApp/single_room.html',{'single_room':single_room, 'messages':messages})

# def room(request, room_name):
#     return render(request, 'chatApp/chatroom.html',{'room_name':room_name})