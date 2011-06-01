# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import State

class StateTestCase(TestCase):
    """Tests for State model"""

    def test_manager(self):
        # start with empty database
        s = State.objects.all()
        self.assertEquals(len(s), 0)
        
        # create a new state, save, fetch & verify
        State(name="New York", population = 99999).save()
        s = State.objects.all()
        self.assertEquals(len(s), 1) 
        s = s[0]
        self.assertEquals(s.name, "New York")
        self.assertEquals(s.slug, "new-york")
        self.assertEquals(s.population, 99999)





