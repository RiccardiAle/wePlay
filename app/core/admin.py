from django.contrib import admin
from core import models
# Register your models here.


@admin.register(models.Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'owner')
    search_fields = ('name', 'address')
    
    
@admin.register(models.SportsField)
class SportsFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'type', 'price', 'indoor')
    search_fields = ('name', 'sport')
