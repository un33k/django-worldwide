# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import City, State, Country

class CityTestCase(TestCase):
    """Tests for City model"""

    def test_manager(self):
        # database has no city
        c = City.objects.all()
        self.assertEquals(len(c), 0)
        
        # create a city and verify
        City(name="New York City", population = 99999).save()
        c = City.objects.all()
        self.assertEquals(len(c), 1) 
        c = c[0]
        self.assertEquals(c.name, "New York City")
        self.assertEquals(c.slug, "new-york-city")
        self.assertEquals(c.population, 99999)
        
        # create two identical cities without states/countries, verify un33k uslug
        City(name="London", population = 10000).save()
        City(name="London", population = 9999).save()
        c = City.objects.filter(name="London")
        self.assertEquals(len(c), 2) 
        self.assertEquals(c[0].slug, "london")
        self.assertEquals(c[1].slug, "london-1")

        # createe two identical cities without state / countries first, verify un33k uslug
        o1 = City(name="Ottawa", population = 8888)
        o1.save()
        o2 = City(name="Ottawa", population = 9999)
        o2.save()
        c = City.objects.filter(name="Ottawa")
        self.assertEquals(len(c), 2) 
        self.assertEquals(c[0].slug, "ottawa")
        self.assertEquals(c[1].slug, "ottawa-1")

        # add different countries to two identical cities and verify un33k uslug
        c1 = Country(name="Canada", iso_2="CA", iso_3="CAN")
        c1.save()
        c2 = Country(name="United States", iso_2="US", iso_3="USA")
        c2.save()
        
        o1.country = c1
        o1.save()
        o2.country = c2
        o2.save()
        c = City.objects.filter(name="Ottawa")
        self.assertEquals(len(c), 2) 
        self.assertEquals(c[0].slug, "ottawa-canada")
        self.assertEquals(c[1].slug, "ottawa-united-states")
        
        # add different states to two identical cities and verify un33k uslug
        s1 = State(name="Ontario")
        s1.save()
        o1.state = s1
        o1.save()
        s2 = State(name="Illinois")
        s2.save()
        o2.state = s2
        o2.save()
        c = City.objects.filter(name="Ottawa")
        self.assertEquals(len(c), 2) 
        self.assertEquals(c[0].slug, "ottawa-ontario-canada")
        self.assertEquals(c[1].slug, "ottawa-illinois-united-states")




         
         
         
        
        
        
