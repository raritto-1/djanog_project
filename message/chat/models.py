from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # Custom primary key
    user_name = models.CharField(max_length=255)  # User's name
    user_email = models.EmailField(unique=True)  # User's email

    def __str__(self):
        return self.user_name


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )  # Reference to the sender (user)
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )  # Reference to the receiver (user)
    text = models.TextField()  # Message content
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for when the message was sent
    
    def __str__(self):
        return f"From {self.sender.user_name} to {self.receiver.user_name}"
