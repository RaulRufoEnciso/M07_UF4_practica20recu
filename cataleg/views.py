from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Productos
from .serializers import ProductosSerializer
# Create your views here.
@api_view(['GET'])
def showAllProducts(request):
    products = Productos.objects.all()
    serializer = ProductosSerializer(products, many=True)
    return Response(serializer.data)

# Muestra los productos en el carrito
@api_view(['GET'])
def showProductoById(request, pk):
    productId = Productos.objects.get(id=pk)
    serializer = ProductosSerializer(productId)
    return Response(serializer.data)

# Mostar el producto en el carrito por Id


@api_view(['POST'])
def addProducto(request):
    serializer = ProductosSerializer(data=request.data, many=False)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Crear los productos en la tabla del carrito

