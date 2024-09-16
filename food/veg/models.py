from django.db import models
from django.contrib.auth.models import User 

class Recipe(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null= True , blank= True)
    recipe_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='images/')  
    
    def __str__(self):
        return self.recipe_name

