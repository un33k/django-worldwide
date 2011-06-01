"""Admin for worldwide"""
from django.contrib import admin
from worldwide.models import Continent
from worldwide.models import Country
from worldwide.models import State
from worldwide.models import City
from worldwide.models import County
from worldwide.models import Ocean
from worldwide.models import Language
from worldwide.models import Currency

from worldwide.admin.continent import ContinentAdmin
from worldwide.admin.country import CountryAdmin
from worldwide.admin.state import StateAdmin
from worldwide.admin.city import CityAdmin
from worldwide.admin.county import CountyAdmin
from worldwide.admin.ocean import OceanAdmin
from worldwide.admin.language import LanguageAdmin
from worldwide.admin.currency import CurrencyAdmin

admin.site.register(Ocean, OceanAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(County, CountyAdmin)
