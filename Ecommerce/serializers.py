from .models import Pais,Categorias,EstadoCompra,Fop,Descuentos,Cupones,Departamentos,Ciudades,Domicilio,Productos,DescuentosDetalle,OrdenDeCompra,DetalleOrdenDeCompra

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    SerializerMethodField
)
from rest_framework import serializers

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ProductosSerializer(ModelSerializer):
    categoria = CategoriasSerializer(many=False)

    class Meta:
        model = Productos
        fields = '__all__'


class OrdenDeCompraSerializer(ModelSerializer):
    class Meta:
        model = OrdenDeCompra
        fields = ['usuario', 'direccion', 'formaPago' , 'estadoCompra', 'estado']