from django.contrib import admin
from worldwide.models import Country

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('full_name',) }
    list_display = ('name', 'slug', 'code', 'capital')
    list_per_page = 25
