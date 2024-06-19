from django.urls import path
from . import views

urlpatterns = [
    # For creating a supplier
    path('create', views.SupplierListCreate.as_view(), name='supplier-view-create'),

    # For updating and viewing a supplier
    path('<int:pk>', views.SupplierRetrieveUpdate.as_view(), name='update'),
]