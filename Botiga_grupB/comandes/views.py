from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comanda
from .serializer import comandasSerializer

@api_view(['GET'])
def historial_compras(request):
    historial = Comanda.objects.filter(comprado=True)
    serializer = comandasSerializer(historial, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def carritos_no_finalizados(request):
    carritos = Comanda.objects.filter(comprado=False)
    serializer = comandasSerializer(carritos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def eliminar_carrito(request, id_carrito):
    # Lógica para eliminar el carrito
    return Response({"message": "Carrito eliminado correctamente"})

@api_view(['POST'])
def finalizar_compra(request, id_comanda):
    try:
        comanda = Comanda.objects.get(id=id_comanda)
        comanda.comprado = True
        comanda.save()
        return Response({"message": "Compra finalizada correctamente"})
    except Comanda.DoesNotExist:
        return Response({"error": "Comanda no encontrada"}, status=404)
