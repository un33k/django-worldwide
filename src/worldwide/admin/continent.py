from django.contrib import admin
from worldwide.models import Continent

class ContinentAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ('name', 'slug', 'code', 'population')
    list_per_page = 25

