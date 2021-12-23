
from django.contrib import admin
from django.db import router
from django.urls import path, include
from cliente.views import clienteviewset
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'cliente', clienteviewset)