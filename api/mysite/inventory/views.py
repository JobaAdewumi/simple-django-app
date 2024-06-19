from django.shortcuts import render
from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()  
    serializer_class = InventorySerializer

class InventoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()  
    serializer_class = InventorySerializer
    lookup_field = 'pk'


# This is a view for regular API

# class InventoryList(APIView):
#     def get(self, request):
#         response_data = Inventory.objects.all()
#         response = {
#             "message": "Inventories",
#             "response": response_data,
#         }

#         return Response(response, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = self.request.data

#         name = data['name']
#         description = data['description']
#         price = data['price']
#         supplier = data['supplier']

#         inventory = Inventory.objects.create(name=name, description=description, price=price, supplier=supplier)

#         inventory.save()

#         response = {
#             "message": "Inventory created successfully",
#             "response": inventory,
#         }

#         return Response(response, status=status.HTTP_201_CREATED)
    
#     def put(self, request, inventory_id):
#         serializer = input.Address(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         response_data = services.address_update(
#             request.user, address_id, **serializer.validated_data
#         )
#         response = {
#             "message": "Address updated successfully",
#             "response": output.AddressUpdate(response_data).data,
#         }

#         return Response(response, status=status.HTTP_200_OK)

#     def delete(self, request, address_id):
#         services.address_delete(request.user, address_id)
#         response = {
#             "message": "Address deleted successfully",
#         }

#         return Response(response, status=status.HTTP_204_NO_CONTENT)

# class AddressUpdateDelete(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, address_id):
#         serializer = input.Address(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         response_data = services.address_update(
#             request.user, address_id, **serializer.validated_data
#         )
#         response = {
#             "message": "Address updated successfully",
#             "response": output.AddressUpdate(response_data).data,
#         }

#         return Response(response, status=status.HTTP_200_OK)

#     def delete(self, request, address_id):
#         services.address_delete(request.user, address_id)
#         response = {
#             "message": "Address deleted successfully",
#         }

#         return Response(response, status=status.HTTP_204_NO_CONTENT)