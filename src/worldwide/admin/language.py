from django.contrib import admin
from worldwide.models import Language

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ('name', 'slug', 'percent', 'dialect')
    list_per_page = 25

