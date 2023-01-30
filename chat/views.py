from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chat_templates/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'chat_templates/room.html', {'room': room, 'messages': messages})
