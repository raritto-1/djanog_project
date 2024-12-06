from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message

def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                sender=form.cleaned_data['sender'],
                receiver=form.cleaned_data['receiver'],
                message=form.cleaned_data['message']
            )
            return redirect('message_success')  # Redirect to a success page
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})

def inbox(request, username):
    received_messages = Message.objects.filter(receiver=username).order_by('-timestamp')
    sent_messages = Message.objects.filter(sender=username).order_by('-timestamp')
    return render(request, 'inbox.html', {
        'received_messages': received_messages,
        'sent_messages': sent_messages,
        'username': username,
    })
