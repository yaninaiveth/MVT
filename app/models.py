from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    parentezco = models.CharField(max_length=50)
    cumple = models.DateField()

    def __str__(self):
        return self.nombre