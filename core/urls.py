from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from frota.api import router as router_frota
from metas.api import router as router_metas
from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("/pdm/", router_metas)
api.add_router("/frota/", router_frota)

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', api.urls),
]
