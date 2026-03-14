from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from metas.api import api  # Importa a API que você criou

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', api.urls), # <--- ESTA LINHA LIGA O BANCO AO SITE
]