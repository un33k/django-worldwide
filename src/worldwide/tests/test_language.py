# -*- coding: utf-8 -*-
from django.test import TestCase
from worldwide.models import Language

class LanguageTestCase(TestCase):
    """Tests for Language model"""

    def test_manager(self):
        # start with empty database
        l = Language.objects.all()
        self.assertEquals(len(l), 0)
        
        # create a new language, save, fetch and verify
        Language(name="English", dialect="Jamaican", percent=33.0).save()
        l = Language.objects.all()
        self.assertEquals(len(l), 1) 
        l = l[0]
        self.assertEquals(l.name, "English")
        self.assertEquals(l.slug, "english")
        self.assertEquals(l.dialect, "Jamaican")
        self.assertEquals(l.percent, 33)

