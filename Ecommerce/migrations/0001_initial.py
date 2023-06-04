# Generated by Django 3.0.6 on 2023-05-30 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(default='', max_length=100, verbose_name='Nombre Categoría:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categorias',
                'ordering': ['nombreCategoria'],
            },
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(default='', max_length=100, verbose_name='Ciudad:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
            ],
            options={
                'verbose_name': 'Ciudades',
                'verbose_name_plural': 'Ciudades',
                'db_table': 'ciudades',
                'ordering': ['ciudad'],
            },
        ),
        migrations.CreateModel(
            name='Cupones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100, verbose_name='Nombre Cupón:')),
                ('descripcion', models.CharField(default='', max_length=100, verbose_name='Descripción:')),
                ('valor', models.FloatField(default=0, verbose_name='$:')),
                ('fechaIni', models.DateField(verbose_name='Fecha Inicio:')),
                ('fechaFin', models.DateField(verbose_name='Fecha Fin:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
            ],
            options={
                'verbose_name': 'Cupones',
                'verbose_name_plural': 'Cupones',
                'db_table': 'cupones',
                'ordering': ['valor'],
            },
        ),
        migrations.CreateModel(
            name='Descuentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=100, verbose_name='Descripción:')),
                ('porcentaje', models.IntegerField(default=0, verbose_name='%:')),
                ('fechaIni', models.DateField(verbose_name='Fecha Inicio:')),
                ('fechaFin', models.DateField(verbose_name='Fecha Fin:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
            ],
            options={
                'verbose_name': 'Descuentos',
                'verbose_name_plural': 'Descuentos',
                'db_table': 'descuentos',
                'ordering': ['porcentaje'],
            },
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(default='', max_length=100, verbose_name='Dirección:')),
                ('barrio', models.CharField(default='', max_length=100, verbose_name='Barrio:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Ciudades')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Domicilio',
                'verbose_name_plural': 'Domicilio',
                'db_table': 'domicilio',
                'ordering': ['direccion'],
            },
        ),
        migrations.CreateModel(
            name='EstadoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoCompra', models.CharField(default='', max_length=50, verbose_name='Estado Compra:')),
                ('descripcion', models.CharField(default='', max_length=150, verbose_name='Descripción:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
            ],
            options={
                'verbose_name': 'Estado de Compra',
                'verbose_name_plural': 'EstadosCompra',
                'db_table': 'estadoCompras',
                'ordering': ['estadoCompra'],
            },
        ),
        migrations.CreateModel(
            name='Fop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formaPago', models.CharField(default='', max_length=50, verbose_name='Forma de Pago:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
            ],
            options={
                'verbose_name': 'Forma de Pago',
                'verbose_name_plural': 'FormaPago',
                'db_table': 'formaPagos',
                'ordering': ['formaPago'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePais', models.CharField(default='', max_length=100, verbose_name='Nombre País:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Paises',
                'db_table': 'pais',
                'ordering': ['nombrePais'],
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100, verbose_name='Nombre:')),
                ('descripcion', models.CharField(default='', max_length=100, verbose_name='Descripción:')),
                ('valor', models.FloatField(default=0, verbose_name='$:')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Categorias')),
            ],
            options={
                'verbose_name': 'Productos',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Domicilio')),
                ('estadoCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.EstadoCompra')),
                ('formaPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Fop')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Orden De Compra',
                'verbose_name_plural': 'OrdenDeCompra',
                'db_table': 'ordenDeCompra',
                'ordering': ['usuario', 'estadoCompra'],
            },
        ),
        migrations.CreateModel(
            name='DetalleOrdenDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
                ('idCupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Cupones', verbose_name='Cupón:')),
                ('idOrdenDeCompra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.OrdenDeCompra', verbose_name='Orden de compra:')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Productos', verbose_name='Producto:')),
            ],
            options={
                'verbose_name': 'Detalle Orden De Compra',
                'verbose_name_plural': 'detalleOrdenDeCompra',
                'db_table': 'detalleOrdenDeCompras',
                'ordering': ['idProducto'],
            },
        ),
        migrations.CreateModel(
            name='DescuentosDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
                ('descuento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Descuentos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Productos')),
            ],
            options={
                'verbose_name': 'Descuentos Detalle',
                'verbose_name_plural': 'DescuentosDetalle',
                'db_table': 'descuentosDetalle',
                'ordering': ['producto', 'descuento'],
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(default='Bogota', max_length=100, verbose_name='Departamento:')),
                ('indicativo', models.IntegerField(default=0, verbose_name='Indicativo:')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado:')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Pais')),
            ],
            options={
                'verbose_name': 'Departamentos',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'departamentos',
                'ordering': ['departamento'],
            },
        ),
        migrations.AddField(
            model_name='ciudades',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Departamentos'),
        ),
    ]