from django.urls import path
from . import views

urlpatterns = [
    # For creating an inventory
    path('create', views.InventoryListCreate.as_view(), name='inventory-view-create'),

    # For updating, reading and deleting an inventory
    path('<int:pk>', views.InventoryRetrieveUpdateDestroy.as_view(), name='update'),
]