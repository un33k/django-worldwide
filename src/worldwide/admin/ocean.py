from django.contrib import admin
from worldwide.models import Ocean

class OceanAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ('name', 'slug', 'area')
    list_per_page = 25