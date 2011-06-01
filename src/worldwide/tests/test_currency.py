# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import Currency

class CurrencyTestCase(TestCase):
    """Tests for Currency model"""

    def test_manager(self):
        # start with empty database
        c = Currency.objects.all()
        self.assertEquals(len(c), 0)
        
        # create a currency, save, fetch & verify
        Currency(name="Dollars", code="$").save()
        c = Currency.objects.all()
        self.assertEquals(len(c), 1) 
        c = c[0]
        self.assertEquals(c.name, "Dollars")
        self.assertEquals(c.slug, "dollars")
        self.assertEquals(c.code, "$")
        
        # create a currency with none ascii code, save, fetch & verify
        Currency(name="Yen", code="¥").save()
        c = Currency.objects.get(code="¥")
        self.assertEquals(c.name, "Yen")
        self.assertEquals(c.slug, "yen")
        self.assertEquals(c.code, u'¥')

