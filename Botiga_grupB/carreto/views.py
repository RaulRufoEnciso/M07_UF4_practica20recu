from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carrito
from .serializers import CarritoSerializer
# Create your views here.
@api_view(["POST"])
def addProductsToCarreto(request):
    serializer = CarritoSerializer(data=request.data, many=False)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("No existe ese producto")
# Añadir productos al carro

@api_view(['GET'])
def showAllProductsInCarrito(request):
    products = Carrito.objects.all()
    serializer = CarritoSerializer(products, many=True)
    return Response(serializer.data)
# Ver productos del carro
