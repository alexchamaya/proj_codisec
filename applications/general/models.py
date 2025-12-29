from django.db import models

# Create your models here.
class General(models.Model):
    mobile = models.CharField('Movil',max_length=15)
    email = models.EmailField('Email',max_length=150)
    address = models.CharField('Direccion',max_length=255)
    created_at = models.DateTimeField('Creado el',auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el',auto_now=True)
    
    class Meta:
        verbose_name = 'Dato General'
        verbose_name_plural = 'Generales'
        ordering = ['-created_at']

    def __str__(self):
        return self.mobile