from django.db import models
from django.contrib.auth.models import User



class profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE )
    Image = models.ImageField(upload_to="user_face/")


    def __str__(self):
        return self.user.username