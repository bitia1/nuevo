from django.db import models
from usuarios.models import Ministro
from iglesia.models import *
from bienesinmuebles import BienInmueble

# Create your models here.
class SolicitudAdquisicionPredio(models.Model):
	opc_adquisicion=(
		('compra','compra'),
		('permuta','permuta'),
		)
	clave=models.CharField(primary_key=True, max_length=50)
	iglesia=models.ForeignKey(Iglesia, null=False, blank=False)
	# Solicitud para la iglesia local o obra:
	obra=models.ForeignKey(Obra,null=True, blank=True)
	modo_de_adquisicion=models.CharField(choices=opc_adquisicion,max_length=50)
	uso=models.TextField()
	doc_acredita_propiedad=models.CharField(max_length=50)
	nombre_propietario=models.CharField(max_length=50)
	domicilio=models.TextField()
	clave_atastral_predio=models.CharField(max_length=50)
	ultimo_recibo_predial=models.FileField(upload_to='archivos')
	superficie_del_predio=models.IntegerField()
	autorización_asuntoslegalesfl=models.FileField(upload_to='archivos')
#-------- Buscar en google maps la localización
	constancia_zonificacion_usodesuelo=models.FileField(upload_to='archivos', null=True,blank=True)
	constancia_alineamiento=models.FileField(upload_to='archivos', null=True,blank=True)
	numero_oficial_terreno=models.CharField(max_length=50, blank=True)
	num_hnos_cercanos=models.IntegerField()
	estatus_solicitud=models.IntegerField(choices=opc_estatus)
	#que viven a 1,500 mts. a la redonda del predio a comprar:


	def __str__(self):
		return self.clave

class SolicitudInicioProyecto(models.Model):
	opc_tramite=(
		('primera','por primera vez'),
		('continuacion','continuacion'),
		)

	iglesia=models.ForeignKey(Iglesia, null=False, blank=False)
	propiedad=models.ForeignKey(BienInmueble)
	obra=models.ForeignKey(Obra,null=True, blank=True)
	ministro=models.ForeignKey(Ministro)
	folio=models.CharField(max_length=50)

	tramite_a_solicitar=models.CharField(choices=opc_tramite,max_length=50)
	fecha=models.DateField() #que la ponga automatica?
	actividad=models.CharField(choices=opc_actividad,max_length=50)
	descripcion=models.TextField()
	predio_clavecatastral=models.CharField(max_length=50)
	ultimo_predial=models.FileField()
	superficie_a_usar=models.IntegerField()
	presupuesto_aprox_proyecto=models.IntegerField()
	servicios=models.TextField()
	capital_inicio=models.IntegerField()
	duracion_aproximada=models.IntegerField()
	materiales_existencia=models.TextField()
	her_activos_eco=models.IntegerField()
	her_manodeobra=models.IntegerField()
	autorizacion_asuntoslegales=models.FileField()
	constancia_zonificaciondeusodesuelo=models.FileField(null=True,blank=True)
	foto1=models.ImageField(upload_to='fotos', null=False)
	foto2=models.ImageField(upload_to='fotos', null=False)
	estatus_solicitud=models.IntegerField(choices=opc_estatus)



	def __str__(self):
		return self.folio
