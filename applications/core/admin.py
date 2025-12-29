from django.contrib import admin
from .models import Miembros


# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    list_display = ('cargo','nombre')
    #list_filter = ('estado',)
    #search_fields = ('nombres','apellidos','cargo')
    readonly_fields = ('created_at','updated_at')


admin.site.register(Miembros, MembersAdmin)