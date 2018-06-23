from django.db import models
from usuarios.models import Ministro
from iglesia.models import *

# Create your models here.
opc_actividad=(
	('mantenimiento','Mantenimiento'),
	('remodelacion','Remodelacion'),
	('ampliacion','Ampliacion'),
	('provicional','Construccion provicional'),
	('definitiva','Construccion definitiva'),
	)
opc_estatus=(
	('1','espera'),
	('2','aprovado por el ministro'),
	('3','rechazado por el ministro'),
	('4','aceptado'),
	('5','denegado')
	)

class BienInmueble(models.Model):

	iglesia=models.ForeignKey(Iglesia, null=False, blank=False)
	obra=models.ForeignKey(Obra,null=True,blank=True)
	clave =models.CharField(max_length=20, primary_key=True)
	entidad_federativa = models.CharField(max_length=50)
	municipio = models.CharField(max_length=50)
	colonia = models.CharField(max_length=50)
	calle_numero = models.CharField(max_length=50)
	cp  = models.IntegerField()
	colindacion_norte = models.CharField(max_length=50)
	colindacion_sur = models.CharField(max_length=50)
	colindacion_este = models.CharField(max_length=50)
	colindacion_oeste = models.CharField(max_length=50)
	# con quien y cuantos metros 
	tipo_documento = models.CharField(max_length=50)
	documento = models.FileField(upload_to='documents/%Y/%m/%d')
	lugar_expedicion = models.CharField(max_length=50)
	fecha_expedicion = models.DateField()
	nombre_propietario = models.CharField(max_length=50)
	situación_juridica = models.CharField(max_length=50)
	superficie_terreno = models.IntegerField()
	superficie_construida = models.IntegerField()
	edificaciones = models.IntegerField()
	niveles = models.IntegerField()
	uso = models.CharField(max_length=50)
	zona = models.CharField(max_length=50)
	servicios = models.TextField()
	foto1 = models.ImageField(upload_to='fotos', null=False)
	foto2 = models.ImageField(upload_to='fotos', null=False)
	foto3 = models.ImageField(upload_to='fotos', null=False)
	foto4 = models.ImageField(upload_to='fotos', null=False)
	lat=models.CharField(max_length=50)
	lng=models.CharField(max_length=50)
#------localizacion

	def __str__(self):
		return self.clave

class RecaudacionFondos(models.Model):
	opc_proposito=(
		('compra','compra de terreno'),
		('construccion_provicional','construccion provicional'),
		('construccion_definitiva','construccion definitiva'),
		('mantenimiento','mantenimiento'),
		('remodelacion','remodelacion'),
		('ampliacion','ampliacion'),
		)
	opc_forma=(
		('colectas','colectas'),
		('ventas','ventas'),
		)
	opc_recaudacion=(
		('activa','activa'), #aun estan recaudando
		('cancelada','cancelada'),#no estan recaudando pero tienen $
		('finalizada','finalizada'),#ya comenzaron el proyecto y el saldo se paso a el saldo del proyecto
		)

	clave=models.CharField(primary_key=True,max_length=50)
	fecha=models.DateField()
	proposito=models.CharField(choices=opc_proposito,max_length=50)
	forma=models.CharField(choices=opc_forma,max_length=50)
	saldo_disponible=models.IntegerField()
	estado=models.CharField(choices=opc_recaudacion,max_length=50)
	iglesia=models.ForeignKey(Iglesia, null=False, blank=False)

	def __str__(self):
		return self.clave

class Proyecto(models.Model):

	opc_estado=(
		('proceso','proceso'),
		('suspendido','suspendido'),
		('cancelado','cancelado'),
		)

	folio = models.CharField(primary_key=True, max_length=50)
	concepto = models.CharField(choices=opc_actividad,max_length=50)
	descripcion = models.TextField()
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField(null=True, blank=True)
	costo_aproximado = models.IntegerField()
	tiempo_aproximado = models.IntegerField()
	estado = models.CharField(choices=opc_estado,max_length=50)
	saldo_disponible= models.IntegerField()

	propiedad = models.ForeignKey(BienInmueble)
	solicitante = models.ForeignKey(Ministro)
	recaudacion= models.OneToOneField(RecaudacionFondos)

	def __str__(self):
		return self.folio

class Reporte(models.Model):

	proyecto =models.ForeignKey(Proyecto)
	ministro =models.ForeignKey(Ministro)

	clave = models.CharField(max_length=40, primary_key=True)
	mes_año =models.CharField(max_length=40)
	saldo_anterior = models.IntegerField(null=True)
	total_ingresos = models.IntegerField(null=True)
	total_salidas = models.IntegerField(null=True) # no puede pones una salida sin factura
	saldo_final = models.IntegerField(null=True)
	fecha_elaboracion = models.DateField(auto_now_add=True)
	donaciones_especie = models.IntegerField()
	estatus = models.IntegerField(choices=opc_estatus) 
	def __str__(self):
		return self.clave

class Factura(models.Model):
	opc_tipo=(
		('efectivo','efectivo'),
		('transferencia','transferencia'),
		)
	
	reporte =  models.ForeignKey(Reporte)
	numero_factura = models.CharField(primary_key=True,max_length=100)

	descripcion = models.TextField()
	rfc_provedor = models.CharField(max_length=50)
	nombre_provedor = models.CharField(max_length=50)
	fecha = models.DateField()
	total = models.IntegerField()
	archivo=models.FileField(upload_to='Facturas', null=False)
	tipo_pago=models.CharField(max_length=50, choices=opc_tipo)

	def __str__(self):
		return self.numero_factura

class ReporteRecaudacion(models.Model):
	clave=models.IntegerField(primary_key=True)
	fecha=models.DateField()
	saldo_anterior=models.IntegerField()
	cantidad_recuadada=models.IntegerField()
	recaudacion=models.ForeignKey(RecaudacionFondos)
	comision=models.ForeignKey(ComisionProConstruccion)

class MaterialEspecie(models.Model):
	clave=models.CharField(max_length=50)
	fecha=models.DateField()
	cantidad=models.CharField(max_length=50)
	costo_aproximado=models.IntegerField()
	descripcion=models.TextField()
	reporte=models.ForeignKey(Reporte)

