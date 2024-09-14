from django.shortcuts import render, redirect
from .models import Recipe

def recipes(request):
    if request.method == "POST":
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')

        
        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description
        )

        
        all_recipes = Recipe.objects.all()
        context = {'recipes': all_recipes}

        
        return render(request, 'recipes.html', context)

    
    all_recipes = Recipe.objects.all()
    context = {'recipes': all_recipes}
    return render(request, 'recipes.html', context)

