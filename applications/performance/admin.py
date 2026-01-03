from django.contrib import admin
from .models import Performance

# Register your models here.
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_performance', 'estado', 'created_at')
    #search_fields = ('title', 'description')
    #list_filter = ('type_performance', 'estado', 'created_at')
    ordering = ('-created_at',)

class AgreementAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_performance', 'estado', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Performance, PerformanceAdmin)
