# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import Country, Continent

class CountryTestCase(TestCase):
    """Tests for Country model"""

    def test_manager(self):
        # start with empty database
        c1 = Country.objects.all()
        self.assertEquals(len(c1), 0)
        
        # create a country, save, fetch again from database and verify
        c1 = Country(name="Canada", iso_2="CA", iso_3="CAN", population = 100000)
        c1.save()
        q1 = Country.objects.get(name="Canada")
        self.assertNotEquals(q1, None)
        self.assertEquals(q1.name, "Canada")
        self.assertEquals(q1.iso_2, "CA")
        self.assertEquals(q1.full_name, "Canada")
        self.assertEquals(q1.slug, "canada")
        self.assertEquals(q1.population, 100000)

        # create second country, save, fetch and verify
        c2 = Country(name="United States", iso_2="US", iso_3="USA", population = 100000)
        c2.full_name = "United States of America"
        c2.save()
        c2 = Country.objects.get(name="United States")
        self.assertEquals(c2.name, "United States")
        self.assertEquals(c2.iso_2, "US")
        self.assertEquals(c2.slug, "united-states")
        self.assertEquals(c2.population, 100000)
        
        # add a continent to an existing country, save, fetch and verify
        c3 = Country.objects.get(name="United States")
        d = Continent(name="North America", code="NA", population=9999999)
        d.save()    
        c3.continent = d
        c3.save()
        c4 = Country.objects.get(continent__slug__exact="north-america")
        self.assertEquals(c4.name, "United States")







