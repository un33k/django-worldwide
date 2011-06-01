# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import Continent

class ContinentTestCase(TestCase):
    """Tests for Continent model"""

    def test_manager(self):
        # start with an empty database
        continents = Continent.objects.all()
        self.assertEquals(len(continents), 0)
        
        # create a continent
        c = Continent()
        c.name = "Europe"
        c.code = "EU"
        c.population = 100000
        c.save()
        
        # search and verify saved continent
        continents = Continent.objects.all()
        self.assertEquals(len(continents), 1) 
        c = continents[0]
        self.assertEquals(c.name, "Europe")
        self.assertEquals(c.code, "EU")
        self.assertEquals(c.slug, "europe")
        self.assertEquals(c.population, 100000)





