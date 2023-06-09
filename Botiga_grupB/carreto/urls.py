from django.urls import path
from . import views

#Rutas del cataleg
urlpatterns = [
    path('add-carreto', views.addProductsToCarreto, name="add-carreto"),
    path('', views.showAllProductsInCarrito, name="show-carreto"),
    path('delete-carrito', views.deleteAllProductosInCarrito, name="delete-carreto"),
    path('delete-product/<str:pk>', views.deleteProductoInCarritoById, name="delete-byId"),
    path('update-carreto/<str:pk>', views.updateProductoInCarrito, name="update-carreto"),
]