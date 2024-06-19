
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/inventory/', include('inventory.urls')),
    path('api/supplier/', include('supplier.urls')),
]
