# views.py
from django.shortcuts import render, get_object_or_404
from .models import UploadImagePost
from .forms import UploadImagePostForm

def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the image to the database
            return render(request, 'success.html')  # Redirect to a success page
    else:
        form = UploadImagePostForm()

    images = UploadImagePost.objects.all()  # Get all images
    return render(request, 'base.html', {'form': form, 'images': images})
