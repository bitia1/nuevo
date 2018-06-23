from django.db import models
from usuarios.models import ComisionInventario, ComisionProConstruccion, Ministro

# Create your models here.
class Iglesia(models.Model):
	clave =models.CharField(max_length=20, primary_key=True)
	estado =models.CharField(max_length=30)
	municipio =models.CharField(max_length=40)
	colonia =models.CharField(max_length=40)
	direccion =models.CharField(max_length=40)
	cp =models.IntegerField()
	telefono_fijo =models.CharField(max_length=14)

	def __str__(self):
		return self.clave

class Obra(models.Model):
	"""docstring for Obra"""
	iglesia = models.ForeignKey(Iglesia)
	clave = models.CharField(primary_key=True, max_length=50)
	estado =models.CharField(max_length=30)
	municipio =models.CharField(max_length=40)
	colonia =models.CharField(max_length=40)
	direccion =models.CharField(max_length=40)
	cp =models.IntegerField()
	telefono_fijo =models.CharField(max_length=14)

class AdministracionMinistro(models.Model):
	numero =models.CharField(max_length=20, primary_key=True)
	iglesia = models.ForeignKey(Iglesia)
	ministro = models.ForeignKey(Ministro)

	inicioadministracion= models.DateField()
	finadministracion= models.DateField(null=True, blank=True)

class AdministracionComisionProconstruccion(models.Model):
	numero =models.CharField(max_length=20, primary_key=True)
	iglesia = models.ForeignKey(Iglesia)
	comision = models.ForeignKey(ComisionProConstruccion)
	
	inicioadministracion= models.DateField()
	finadministracion= models.DateField(null=True, blank=True)

class AdministracionComisionInventario(models.Model):
	numero =models.CharField(max_length=20, primary_key=True)
	iglesia = models.ForeignKey(Iglesia)
	comision= models.ForeignKey(ComisionInventario)
	
	inicioadministracion= models.DateField(null=False,blank=False)
	finadministracion= models.DateField(null=True, blank=True)

# tesoreria(solo ve reportes de proconstruccion)