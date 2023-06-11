from django.urls import path
from .views import historial_compras, carritos_no_finalizados, eliminar_carrito, finalizar_compra

urlpatterns = [
    path('historial-compras/', historial_compras, name='historial_compras'),
    path('carritos-no-finalizados/', carritos_no_finalizados, name='carritos_no_finalizados'),
    path('eliminar-carrito/<int:id_carrito>/', eliminar_carrito, name='eliminar_carrito'),
    path('finalizar-compra/<int:id_comanda>/', finalizar_compra, name='finalizar_compra'),
]
