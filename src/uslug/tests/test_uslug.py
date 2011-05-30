# -*- coding: utf-8 -*-
"""Unit tests for uslug"""
from django.test import TestCase
from django.template import Context, Template
from uslug import uSlug

class SlugTestCase(TestCase):
    """Tests for Slug"""

    def test_manager(self):
        s = "This is a test ---"
        r = uSlug(s)
        self.assertEquals(r, "this-is-a-test")

        s = 'C\'est déjà l\'été.'
        r = uSlug(s)
        self.assertEquals(r, "c-est-deja-l-ete")
        
        s = 'Nín hǎo. Wǒ shì zhōng guó rén'
        r = uSlug(s)
        self.assertEquals(r, "nin-hao-wo-shi-zhong-guo-ren")

        s = '影師嗎'
        r = uSlug(s)
        self.assertEquals(r, "ying-shi-ma")     