from django.contrib import admin
from .models import Plan

# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_at')
    readonly_fields = ('created_at','updated_at')

admin.site.register(Plan, PlanAdmin)