from django.contrib import admin
from worldwide.models import State

class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ('name', 'slug', 'code', 'capital')
    list_per_page = 25
