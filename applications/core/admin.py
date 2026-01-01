from django.contrib import admin
from .models import Miembros, Carrousel


# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    list_display = ('cargo','nombre')
    #list_filter = ('estado',)
    #search_fields = ('nombres','apellidos','cargo')
    readonly_fields = ('created_at','updated_at')


class CarrouselAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle','estado')
    #list_filter = ('estado',)
    readonly_fields = ('created_at','updated_at')

admin.site.register(Miembros, MembersAdmin)
admin.site.register(Carrousel, CarrouselAdmin)