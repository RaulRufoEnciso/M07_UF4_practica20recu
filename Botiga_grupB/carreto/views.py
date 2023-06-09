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

@api_view(['DELETE'])
def deleteProductoInCarritoById(request, pk):
    product = Carrito.objects.get(id=pk)
    product.delete()
    return Response("Producto eliminado del carrito con exito")

# Elimina un producto del carrito

@api_view(['DELETE'])
def deleteAllProductosInCarrito(request):
    product = Carrito.objects.all()
    product.delete()
    return Response("Productos eliminados del carrito con exito")

# Elimina todos los productos del carrito

@api_view(['GET','POST'])
def updateProductoInCarrito(request, pk):
    product = Carrito.objects.get(id=pk)
    serializer = CarritoSerializer(instance=product, data=request.data, many=False)

    if not serializer.is_valid():
        return Response("No se pudo modificar, prueba a modificar los campos de Cantidad y Comprado")
    else:
        serializer.save()
        return Response(serializer.data)
    return Response("Prueba a modificar los campos de Cantidad y Comprado")

# Editar los productos en en carrito para modificar cantidad y estado de vendido

@api_view(['GET'])
def checkIfCompradoIsTrue(request, pk):
    comprado = Carrito.objects.get(id=pk).comprado
    if comprado != True:
        return Response("El articulo no esta comprado")
    return Response("El articulo se compro correctamente")

# Editar los productos en en carrito para modificar cantidad y estado de vendido
