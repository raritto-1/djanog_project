from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as django_messages
from django.contrib.auth.decorators import login_required
from .models import User, Message
from .forms import MessageForm
from django.db.models import Q  # For filtering messages between users

@login_required
def chat_home(request):
    """
    Display all users available for chatting.
    """
    users = User.objects.all()
    return render(request, 'chat_home.html', {'users': users})


@login_required
def chat_room(request, sender_id, receiver_id):
    """
    Display the chat room for a conversation between a sender and a receiver.
    """
    sender = get_object_or_404(User, pk=sender_id)
    receiver = get_object_or_404(User, pk=receiver_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Create and save the message
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                text=form.cleaned_data['message']
            )
            django_messages.success(request, 'Message sent successfully!')
            return redirect('chat_room', sender_id=sender_id, receiver_id=receiver_id)
        else:
            django_messages.error(request, 'There was an error with your message. Please try again.')

    else:
        form = MessageForm()

    # Fetch messages between the sender and receiver
    chat_messages = Message.objects.filter(
        Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender)
    ).order_by('timestamp')

    return render(request, 'chat_room.html', {
        'form': form,
        'sender': sender,
        'receiver': receiver,
        'messages': chat_messages
    })
