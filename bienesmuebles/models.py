from django.db import models
from iglesia.models import Iglesia, Obra
from usuarios.models import Ministro
	
class Mueble(models.Model):
	iglesia=models.ForeignKey(Iglesia,default=0)
	obra=models.ForeignKey(Obra,null=True, blank=True)
	clave=models.CharField(primary_key=True, max_length=50)
	nombre = models.CharField(max_length=50)
	area= models.CharField(max_length=50)
	subarea= models.CharField(max_length=50)
	descripcion= models.TextField()
	estado= models.CharField(max_length=50)
	marca= models.CharField(max_length=50)
	material= models.CharField(max_length=50)
	tamano_metros= models.IntegerField()
	tiempo_vida= models.IntegerField()
	tipo= models.CharField(max_length=50)
	valor_estimado= models.IntegerField()
	imagen=models.ImageField(upload_to='fotos', null=True)
	activo=models.BooleanField(default=True)

	def __str__(self):
		return self.clave


# para eliminar un bien mueble o comprar un mueble si es mayor a $6000 tendra que hacer una solicitud
class SolicitudCompra(models.Model):
	ministro=models.ForeignKey(Ministro)
	iglesia=models.ForeignKey(Iglesia)
	clave_solicitud=models.CharField(primary_key=True, max_length=50)
	obra=models.ForeignKey(Obra, null=True, blank=True)
	area=models.CharField(max_length=50)
	descripcion=models.TextField()
	costo_aproximado=models.IntegerField()
	fotografia1=models.ImageField()
	fotografia2=models.ImageField()
	estado_solicitud=models.CharField(max_length=50)
	def __str__(self):
		return self.clave_solicitud

class SolicitudBaja(models.Model):
	ministro=models.ForeignKey(Ministro)
	iglesia=models.ForeignKey(Iglesia)
	clave_solicitud=models.CharField(primary_key=True, max_length=50)
	obra=models.ForeignKey(Obra, null=True, blank=True)
	mueble=models.ForeignKey(Mueble)
	razon=models.CharField(max_length=70)
	estado_solicitud=models.CharField(max_length=50)
	def __str__(self):
		return self.clave_solicitud