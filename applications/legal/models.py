from django.db import models

# Create your models here.
class Norms(models.Model):
    title = models.CharField('Norma Legal',max_length=100)
    description = models.CharField('Descripción',max_length=250)
    file = models.FileField('Archivo',upload_to='norms/')
    created_at = models.DateTimeField('Creado el',auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el',auto_now=True)

    class Meta:
        verbose_name = "Norma Legal"
        verbose_name_plural = "Normas Legales"
        ordering = ['created_at']

    def __str__(self):
        return self.title