from django.contrib import admin
from worldwide.models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ('name', 'slug', 'code')
    list_per_page = 25

