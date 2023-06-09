from django.urls import path
from . import views

#Rutas del cataleg
urlpatterns = [
    path('add-carreto', views.addProductsToCarreto, name="add-carreto"),
    path('', views.showAllProductsInCarrito, name="show-carreto"),

]