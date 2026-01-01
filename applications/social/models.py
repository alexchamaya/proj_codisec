from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField('Nombre clave', max_length=50, unique=True)
    name = models.CharField('Red Social', max_length=200)
    url = models.URLField('Enlace',max_length=200, null=True, blank=True)
    created_at = models.DateTimeField('Creado el', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True)
    
    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['-created_at']

    def __str__(self):
        return self.name