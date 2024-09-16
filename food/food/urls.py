"""
URL configuration for computer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from veg import views as veg_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
       
    path('', veg_views.recipes, name='recipes'),
    path('recipes/delete/<int:recipe_id>/', veg_views.delete_recipe, name='delete_recipe'),
    path('login', veg_views.login_page, name='login'),
    path('register', veg_views.register_page, name='register'),
    path('admin/', admin.site.urls),
    path('logout/', veg_views.log_out, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


