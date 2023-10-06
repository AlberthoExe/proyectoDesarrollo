from django.db import models

# Create your models here.

from bases.models import Clasemodelo

class Categoria(Clasemodelo):
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripcion de la categoria",
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"



class SubCategoria(Clasemodelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria'
    )

    def __str__(self):
        return '{},{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')


class Marca(Clasemodelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion=self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"


class UnidadMedida(Clasemodelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion=self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidad de Medida"