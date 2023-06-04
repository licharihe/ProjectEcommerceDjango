from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from .choices import estados

# Create your models here.
class Pais(models.Model):
    nombrePais = models.CharField(max_length=100,verbose_name='Nombre País:',default='')
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')

    def nombre_Pais(self):
        return "{}" .format(self.nombrePais)

    def  __str__(self):
        return self.nombre_Pais()

    class Meta:
        verbose_name='País'
        verbose_name_plural ='Paises'
        db_table='pais'
        ordering=['nombrePais']

class Categorias(models.Model):
    nombreCategoria = models.CharField(max_length=100,verbose_name='Nombre Categoría:',default='')
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')

    def nombre_Categoria(self):
        return "{}" .format(self.nombreCategoria)

    def  __str__(self):
        return self.nombre_Categoria()

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural ='Categorias'
        db_table='categorias'
        ordering=['nombreCategoria']

class EstadoCompra(models.Model):
    estadoCompra = models.CharField(max_length=50,verbose_name='Estado Compra:',default='')
    descripcion = models.CharField(max_length=150,verbose_name='Descripción:',default='')
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')

    def nombre_EstadoCompra(self):
        return "{}" .format(self.estadoCompra)

    def  __str__(self):
        return self.nombre_EstadoCompra()

    class Meta:
        verbose_name='Estado de Compra'
        verbose_name_plural ='EstadosCompra'
        db_table='estadoCompras'
        ordering=['estadoCompra']

class Fop(models.Model):
    formaPago = models.CharField(max_length=50,verbose_name='Forma de Pago:',default='')
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')

    def nombre_Fop(self):
        return "{}" .format(self.formaPago)

    def  __str__(self):
        return self.nombre_Fop()

    class Meta:
        verbose_name='Forma de Pago'
        verbose_name_plural ='FormaPago'
        db_table='formaPagos'
        ordering=['formaPago']



class Descuentos(models.Model):
    descripcion = models.CharField(max_length=100,verbose_name='Descripción:',default='')
    porcentaje = models.IntegerField(verbose_name='%:',default=0)
    fechaIni = models.DateField(verbose_name='Fecha Inicio:')
    fechaFin = models.DateField(verbose_name='Fecha Fin:')
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')

    def nombre_Descuentos(self):
        return "{} , {}% , {} , {}" .format(self.descripcion,self.porcentaje,self.fechaIni,self.fechaFin)

    def  __str__(self):
        return self.nombre_Descuentos()

    class Meta:
        verbose_name='Descuentos'
        verbose_name_plural ='Descuentos'
        db_table='descuentos'
        ordering=['porcentaje']


class Cupones(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre Cupón:',default='')
    descripcion = models.CharField(max_length=100,verbose_name='Descripción:',default='')
    valor = models.FloatField(verbose_name='$:',default=0)
    fechaIni = models.DateField(verbose_name='Fecha Inicio:')
    fechaFin = models.DateField(verbose_name='Fecha Fin:')
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')

    def nombre_Cupones(self):
        return "{} , {} , {} , {} ,{}" .format(self.nombre,self.descripcion,self.valor,self.fechaIni,self.fechaFin)

    def  __str__(self):
        return self.nombre_Cupones()

    class Meta:
        verbose_name='Cupones'
        verbose_name_plural ='Cupones'
        db_table='cupones'
        ordering=['valor']


class Departamentos(models.Model):    
    pais=models.ForeignKey(Pais,null =False,blank=False,on_delete=models.CASCADE)
    #departamento = models.CharField(max_length=100,verbose_name='Departamento:',default='') 
    departamento = models.CharField(max_length=100,verbose_name='Departamento:',default='Bogota') 
    indicativo = models.IntegerField(verbose_name='Indicativo:',default=0) 
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')
   

    def nombre_Departamentos(self):
        return "{}" .format(self.departamento)

    def  __str__(self):
        return self.nombre_Departamentos()

    class Meta:
        verbose_name='Departamentos'
        verbose_name_plural ='Departamentos'
        db_table='departamentos'
        ordering=['departamento']



class Ciudades(models.Model):    
    departamento=models.ForeignKey(Departamentos,null =False,blank=False,on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=100,verbose_name='Ciudad:',default='')    
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')
   

    def nombre_Ciudades(self):
        return "{}" .format(self.ciudad)

    def  __str__(self):
        return self.nombre_Ciudades()

    class Meta:
        verbose_name='Ciudades'
        verbose_name_plural ='Ciudades'
        db_table='ciudades'
        ordering=['ciudad']


class Domicilio(models.Model):       
    usuario = models.OneToOneField(User,null =False,blank=False, on_delete=models.CASCADE)
    ciudad=models.ForeignKey(Ciudades,null =False,blank=False,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100,verbose_name='Dirección:',default='')    
    barrio = models.CharField(max_length=100,verbose_name='Barrio:',default='')      
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')
   

    def nombre_Domicilio(self):
        return "{}  {} , {} , {} , {}" .format(self.usuario.first_name,self.usuario.last_name,self.ciudad,self.direccion,self.barrio)

    def  __str__(self):
        return self.nombre_Domicilio()

    class Meta:
        verbose_name='Domicilio'
        verbose_name_plural ='Domicilio'
        db_table='domicilio'
        ordering=['direccion']


class Productos(models.Model):    
    categoria=models.ForeignKey(Categorias,null =False,blank=False,on_delete=models.CASCADE)    
    nombre = models.CharField(max_length=100,verbose_name='Nombre:',default='')    
    descripcion = models.CharField(max_length=100,verbose_name='Descripción:',default='')    
    valor = models.FloatField(verbose_name='$:',default=0)  
    cantidad = models.IntegerField(verbose_name='Cantidad:',default=0) 
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')
    image = models.ImageField(upload_to='imagesProducts/' ,null=True)

    def nombre_Productos(self):
        return "{} , ${} , {}" .format(self.nombre,self.valor,self.cantidad)

        #return "{} , {} , {}" .format(self.nombre,self.valor,self.cantidad)

    def  __str__(self):
        return self.nombre_Productos()

    class Meta:
        verbose_name='Productos'
        verbose_name_plural ='Productos'
        db_table='productos'
        ordering=['nombre']


class DescuentosDetalle(models.Model):    
    producto=models.ForeignKey(Productos,null =False,blank=False,on_delete=models.CASCADE)    
    descuento=models.ForeignKey(Descuentos,null =False,blank=False,on_delete=models.CASCADE)    
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')
   

    def nombre_DescuentosDetalle(self):
        return "{} , {}" .format(self.producto,self.descuento)

    def  __str__(self):
        return self.nombre_DescuentosDetalle()

    class Meta:
        verbose_name='Descuentos Detalle'
        verbose_name_plural ='DescuentosDetalle'
        db_table='descuentosDetalle'
        ordering=['producto','descuento']


class OrdenDeCompra(models.Model):    
    usuario = models.OneToOneField(User,null =False,blank=False, on_delete=models.CASCADE)
    direccion=models.ForeignKey(Domicilio,null =False,blank=False,on_delete=models.CASCADE)  
    formaPago=models.ForeignKey(Fop,null =False,blank=False,on_delete=models.CASCADE)   
    estadoCompra=models.ForeignKey(EstadoCompra,null =False,blank=False,on_delete=models.CASCADE)       
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')
   

    def nombre_OrdenDeCompra(self):
        return "{} , {} , {}" .format(self.direccion,self.formaPago,self.estadoCompra)

    def  __str__(self):
        return self.nombre_OrdenDeCompra()

    class Meta:
        verbose_name='Orden De Compra'
        verbose_name_plural ='OrdenDeCompra'
        db_table='ordenDeCompra'
        ordering=['usuario','estadoCompra']

class DetalleOrdenDeCompra(models.Model):    
    idOrdenDeCompra = models.OneToOneField(OrdenDeCompra,null =False,blank=False, on_delete=models.CASCADE,verbose_name='Orden de compra:')
    idProducto=models.ForeignKey(Productos,null =False,blank=False,on_delete=models.CASCADE,verbose_name='Producto:')  
    idCupon=models.ForeignKey(Cupones,null =False,blank=False,on_delete=models.CASCADE,verbose_name='Cupón:')   
    cantidad = models.IntegerField(verbose_name='Cantidad:',default=0)      
    estado=models.CharField(max_length=1, choices=estados, default='A',verbose_name='Estado:')
   

    def nombre_OrdenDeCompra(self):
        return "{} , {} , {} , {}" .format(self.idOrdenDeCompra,self.idProducto,self.idCupon,self.cantidad)

    def  __str__(self):
        return self.nombre_OrdenDeCompra()

    class Meta:
        verbose_name='Detalle Orden De Compra'
        verbose_name_plural ='detalleOrdenDeCompra'
        db_table='detalleOrdenDeCompras'
        ordering=['idProducto']

