from django.urls import path

from django.urls import re_path
from .views import categoriaListApi, productoListApi, ordenDeCompraSerializer,ProductosCreateApi

app_name = 'Ecommerce'

urlpatterns = [
    re_path(r"^getproducts$", productoListApi.as_view(), name="getproducts"),
    re_path(r"^getcategories", categoriaListApi.as_view(), name="getcategories"),
    re_path(r"^OrdenDecompra", ordenDeCompraSerializer.as_view(), name="ordenDecompra"),
    re_path(r"^Productos", ProductosCreateApi.as_view(), name="Productos"),
]