from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='images/')  
    
    def __str__(self):
        return self.recipe_name

