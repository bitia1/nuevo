from django.shortcuts import render
from  django.http  import  HttpResponseRedirect
from  django.views.generic  import  View
from .forms import MuebleForm
# Create your views here.

def homeview(request):
	return render(request, 'homeBM.html')


class ArtuculoView(View):
    ''' OrganizacionEstudio '''
    form_class= MuebleForm
    initial=''
    errores=[]
    template_name = 'register.html'
    cont=0
    respuesta=0

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        usuario=request.user
        if form.is_valid():
            form=form.save()
            form.usuario=usuario
            form.save()

            cont=Contador(form)
            respuesta=valores(0,cont)
            print("contando los no    ",cont, "Respuesta      ",respuesta)
            form.diagnostico=respuesta
            form.save(update_fields=["diagnostico"])
            print("guardado")

            return HttpResponseRedirect("/anexo13/gracias/")
        else:
            self.errores.append(form.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})
            