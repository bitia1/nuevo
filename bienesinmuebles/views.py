from django.shortcuts import render
from django.views.generic import FormView

from bienesinmuebles.forms import BienesInmueblesForm


class BienesInmueblesmView(FormView):
    form_class = BienesInmueblesForm
    template_name = 'mapa.html'
