from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

# Create your views here.

@login_required
def chat_room(request):
    # Retrieve the latest 5 messages
    latest_messages = Message.objects.select_related('user').order_by('-id')[:5]
    latest_messages = reversed(latest_messages)
    return render(
        request,
        'chat/room.html',
        {'latest_messages': latest_messages}
    )
