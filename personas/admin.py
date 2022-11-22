from django.contrib import admin
from .models import Persona

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_per_page = 9
    search_fields = ('nombre', 'apellido')
    list_display = ('nombre', 'apellido')
    fields = ('nombre', 'apellido')
    list_display_links = ('apellido',)

admin.site.register(Persona, PersonaAdmin)
