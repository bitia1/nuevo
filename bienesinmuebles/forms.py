from django.forms import ModelForm
from .models import BienInmueble

class BienesInmueblesForm(ModelForm):
	class Meta:
		model =BienInmueble
		exclude=["iglesia","obra","clave"]