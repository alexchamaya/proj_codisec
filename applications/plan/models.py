from django.db import models

# Create your models here.
class Plan(models.Model):
    title = models.CharField('Titulo',max_length=100)
    description = models.CharField('Descripción',max_length=250)
    file = models.FileField('Archivo',upload_to='plan/')
    created_at = models.DateTimeField('Creado el',auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el',auto_now=True)

    class Meta:
        verbose_name = "Plan Provincial"
        verbose_name_plural = "Plan Provincial"
        ordering = ['created_at']

    def __str__(self):
        return self.title