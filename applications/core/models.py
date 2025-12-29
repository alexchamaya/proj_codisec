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