from django.contrib import admin
from usuarios.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Ministro)
admin.site.register(ComisionProConstruccion)
admin.site.register(ComisionInventario)