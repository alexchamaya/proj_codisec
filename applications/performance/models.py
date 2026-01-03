from django.db import models

# Create your models here.
class Performance(models.Model):
    TYPE_PERFORMANCE = {
        "A": "Acuerdo",
        "E": "Evaluación",
    }
    title = models.CharField('Titulo', max_length=100)
    description = models.CharField('Descripción', max_length=250)
    type_performance = models.CharField('Tipo', max_length=1, choices=TYPE_PERFORMANCE)
    file = models.FileField('Archivo', upload_to='performance/')
    estado = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        verbose_name = "Desempeño"
        verbose_name_plural = "Informes de Desempeño"
        ordering = ['-created_at']

    def __str__(self):
        return self.title