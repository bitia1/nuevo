from django.db import models

# Create your models here.
# from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_ministro = models.BooleanField(default=False)
    is_comisionproconstruccion = models.BooleanField(default=False)
    is_comisioninventario = models.BooleanField(default=False)
    

    def get_ministro_profile(self):
        ministro_profile = None
        if hasattr(self, 'ministro'):
            ministro_profile = self.ministro
        return ministro_profile

    def get_comisionpro_profile(self):
        comisionpro_profile = None
        if hasattr(self, 'comisionproconstruccion'):
            comisionpro_profile = self.comisionproconstruccion
        return comisionpro_profile

    def get_comisioninventario_profile(self):
        comisioninventario_profile = None
        if hasattr(self, 'comisioninventario'):
            comisioninventario_profile = self.comisioninventario
        return comisioninventario_profile

    class Meta:
        db_table = 'auth_user'


class Ministro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grado = models.CharField(max_length=40)
    telefono = models.CharField(max_length=14)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        nom=self.user.username+" "+self.user.first_name+" "+self.user.last_name
        return nom
class ComisionProConstruccion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=14)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        nom=self.user.username+" "+self.user.first_name+" "+self.user.last_name
        return nom

class ComisionInventario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=14)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        nom=self.user.username+" "+self.user.first_name+" "+self.user.last_name
        return nom