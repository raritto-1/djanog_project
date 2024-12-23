# models.py
from django.db import models

class UploadImagePost(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title
