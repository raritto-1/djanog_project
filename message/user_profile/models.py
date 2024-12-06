from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pic/", null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_name(self):
        """
        Returns the display name if it exists; otherwise, returns the username.
        """
        return self.displayname if self.displayname else self.user.username

    def get_avatar(self):
        """
        Returns the URL of the profile image if it exists; otherwise, returns the default avatar URL.
        """
        return self.image.url if self.image else f'{settings.STATIC_URL}images/avatar.svg'