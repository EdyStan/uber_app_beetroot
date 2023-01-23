from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room, Message


@login_required
def rooms(request):
    all_rooms = Room.objects.all()

    return render(request, 'chat_templates/rooms.html', {'rooms': all_rooms})


@login_required
def room(request, slug):
    chosen_room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat_templates/room.html', {'room': chosen_room, 'messages': messages})
