from django.urls import path
from . import views

#Rutas del cataleg
urlpatterns = [
    path('', views.showAllProducts, name="producto"),
    path('producto/<str:pk>/', views.showProductoById, name="productoId"),
  
]