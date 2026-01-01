from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at', 'updated_at')
    #search_fields = ('name', 'key')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
admin.site.register(Link, LinkAdmin)