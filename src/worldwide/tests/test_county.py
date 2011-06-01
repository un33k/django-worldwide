# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import County

class CountyTestCase(TestCase):
    """Tests for County model"""

    def test_manager(self):
        # start with an empty county
        c = County.objects.all()
        self.assertEquals(len(c), 0)
        
        # create a county, save, fetch and verify
        County(name="San Francisco").save()
        c = County.objects.all()
        self.assertEquals(len(c), 1) 
        c = c[0]
        self.assertEquals(c.name, "San Francisco")
        self.assertEquals(c.slug, "san-francisco")






