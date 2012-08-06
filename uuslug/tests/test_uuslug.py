# -*- coding: utf-8 -*-
"""Unit tests for uslug"""
from django.test import TestCase
from django.template import Context, Template
from uuslug.models import CoolSlug 
from uuslug import uuslug as slugify

class SlugUnicodeTestCase(TestCase):
    """Tests for Slug - Unicode"""

    def test_manager(self):
        s = "This is a test ---"
        r = slugify(s)
        self.assertEquals(r, "this-is-a-test")

        s = 'C\'est déjà l\'été.'
        r = slugify(s)
        self.assertEquals(r, "cest-deja-lete")

        s = 'Nín hǎo. Wǒ shì zhōng guó rén'
        r = slugify(s)
        self.assertEquals(r, "nin-hao-wo-shi-zhong-guo-ren")

        s = '影師嗎'
        r = slugify(s)
        self.assertEquals(r, "ying-shi-ma")

class SlugUniqueTestCase(TestCase):
    """Tests for Slug - Unique"""

    def test_manager(self):
        name = "john"
        c = CoolSlug.objects.create(name=name)
        c.save()
        self.assertEquals(c.slug, name)
       
        c1 = CoolSlug.objects.create(name=name)
        c1.save()
        self.assertEquals(c1.slug, name+"-1")




