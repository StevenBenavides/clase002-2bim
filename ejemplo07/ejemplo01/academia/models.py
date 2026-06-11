from django.db import models

# Create your models here.
from django.db import models

from datetime import datetime

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()


#representamos los objetos 
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.verificar_cedula()} - {self.edad} - {self.obtener_anio() }"
   

    def obtener_anio(self):
        obtener_actual = datetime.now().year
        valor = obtener_actual - self.edad
        return valor
    
    def verificar_cedula(self):
        primeros_digitos = self.cedula[0:2]
        if primeros_digitos == "11":
            return "Loja"
        return "Otra ciudad"

