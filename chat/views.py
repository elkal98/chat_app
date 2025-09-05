from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from .models import Message
from .forms import SignUpForm

User = get_user_model()

@login_required
def chat_room(request):
    # Latest 20 messages
    latest_messages = Message.objects.select_related('user').order_by('-id')[:20]
    latest_messages = reversed(latest_messages)

    # All users except self (for recipient dropdown)
    users = User.objects.exclude(id=request.user.id)

    return render(
        request,
        'chat/room.html',
        {
            'latest_messages': latest_messages,
            'users': users,
        }
    )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat:chat_room')
        return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

