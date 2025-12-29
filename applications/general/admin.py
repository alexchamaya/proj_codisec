from django.contrib import admin
from .models import General

# Register your models here.
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('mobile','email','address')
    #search_fields = ('mobile','email','address')
    readonly_fields = ('created_at','updated_at')

admin.site.register(General, GeneralAdmin)