from django.shortcuts import render
from django.http import JsonResponse
import base64
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        face_image_data = request.POST.get("face_image")
        
        # Data comes in base64, so we decode it
        face_image_data = face_image_data.split(",")[1]
        face_image = ContentFile(base64.b64decode(face_image_data), name=f'{username}_.jpg')

        try:
            user = User.objects.create(username=username)
        except Exception as e:  # Handles cases like unique constraint violation
            return JsonResponse({"message": "Username is already taken"}, status=400)

        profile.objects.create(user=user, face_image=face_image)
        return JsonResponse({"message": "You have registered successfully"}, status=201)

    return render(request, "register.html")
