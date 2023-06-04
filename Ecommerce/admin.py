from django.contrib import admin

# Register your models here.
from .models import Pais,Categorias,EstadoCompra,Fop,Descuentos,Cupones,Departamentos,Ciudades,Domicilio,Productos,DescuentosDetalle,OrdenDeCompra,DetalleOrdenDeCompra

# Create your models here.
admin.site.register(Pais)
admin.site.register(Categorias)
admin.site.register(EstadoCompra)
admin.site.register(Fop)
admin.site.register(Descuentos)
admin.site.register(Cupones)
admin.site.register(Departamentos)
admin.site.register(Ciudades)
admin.site.register(Domicilio)
admin.site.register(Productos)
admin.site.register(DescuentosDetalle)
admin.site.register(OrdenDeCompra)
admin.site.register(DetalleOrdenDeCompra)