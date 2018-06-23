from django import forms
from .models import Mueble

class MuebleForm(forms.ModelForm):
	class Meta:
		model=Mueble
		exclude=["clave","iglesia"]