from django.contrib import admin
from .models import Norms
# Register your models here.
class NormsAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_at')
    readonly_fields = ('created_at','updated_at')
    
admin.site.register(Norms, NormsAdmin)
