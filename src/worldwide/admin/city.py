from django.contrib import admin
from worldwide.models import City

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ('name', 'slug', 'state', 'country', 'county')
    list_per_page = 25