from django.db import models

# Create your models here.
class Miembros(models.Model):
    cargo = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.cargo} {self.nombre}"


class Carrousel(models.Model):
    title = models.CharField('Titulo',max_length=150)
    subtitle = models.CharField('Subtitulo', max_length=100)
    imagen = models.ImageField('Imagen 1439px x 850px',upload_to='carrousel/')
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField('Creado el',auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el',auto_now=True)
    
    class Meta:
        verbose_name = "Carrousel"
        verbose_name_plural = "Carrousels"
        ordering = ['created_at']

    def __str__(self):
        return self.title