from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": 'bhaiya is great',
        "variable1": ' lalit bhaiya is great'
    }
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse ('this is my  aboutpage')
    return render(request, 'about.html', )

def services(request):
    # return HttpResponse ('i am your servent')
    return render(request, 'services.html',)

def contact(request):
    # return HttpResponse('its my number - 9772312086')
    return render(request, 'contact.html', )