from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group, User

from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView

from .models import Categorias, OrdenDeCompra, Productos
from .serializers import  CategoriasSerializer, ProductosSerializer,OrdenDeCompraSerializer
# Create your views here.



@permission_classes((AllowAny,))
class productoListApi(ListAPIView):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.filter(valor__lte=5000000, valor__gte=1000000)


@permission_classes((AllowAny,))
class categoriaListApi(ListAPIView):
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all().order_by('nombreCategoria')


@permission_classes((AllowAny,))
class ordenDeCompraSerializer(CreateAPIView):
    queryset = OrdenDeCompra.objects.all()
    serializer_class = OrdenDeCompraSerializer


@permission_classes((AllowAny,))
class ProductosCreateApi(CreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer