# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import Ocean

class OceanTestCase(TestCase):
    """Tests for Ocean model"""

    def test_manager(self):
        # start with empty database
        o = Ocean.objects.all()
        self.assertEquals(len(o), 0)
        
        # create an ocean, save, fetch and verify
        o = Ocean(name="Indian Ocean", area=100001)
        o.save()
        o = Ocean.objects.all()
        self.assertEquals(len(o), 1) 
        o = o[0]
        self.assertEquals(o.name, "Indian Ocean")
        self.assertEquals(o.slug, "indian-ocean")
        self.assertEquals(o.area, 100001)



