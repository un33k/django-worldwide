from django.contrib import admin
from worldwide.models import County

class CountyAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ('name', 'slug')
    list_per_page = 25

