# -*- coding: utf-8 -*-

from django.test import TestCase

# http://pypi.python.org/pypi/django-tools/
#from django_tools.unittest_utils.print_sql import PrintQueries

from uuslug.models import CoolSlug, AnotherSlug
from uuslug import slugify


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
        
        s = 'Компьютер'
        r = slugify(s)
        self.assertEquals(r, "kompiuter")


class SlugUniqueTestCase(TestCase):
    """Tests for Slug - Unique"""
    
    def test_manager(self):
        name = "john"

        #with PrintQueries("create first john"): # display the SQL queries
        with self.assertNumQueries(2):
            # 1. query: SELECT test, if slug 'john' exists
            # 2. query: INSERT values
            obj = CoolSlug.objects.create(name=name)
        self.assertEquals(obj.slug, "john")

        #with PrintQueries("create second john"): # display the SQL queries
        with self.assertNumQueries(3):
            # 1. query: SELECT test, if slug 'john' exists
            # 2. query: SELECT test, if slug 'john-1' exists
            # 3. query: INSERT values
            obj = CoolSlug.objects.create(name=name)
        self.assertEquals(obj.slug, "john-1")

    def test_start_no(self):
        name = 'Foo Bar'

        #with PrintQueries("create first 'Foo Bar'"): # display the SQL queries
        with self.assertNumQueries(2):
            # 1. query: SELECT test, if slug 'foo-bar' exists
            # 2. query: INSERT values
            obj = AnotherSlug.objects.create(name=name)
        self.assertEquals(obj.slug, "foo-bar")

        #with PrintQueries("create second 'Foo Bar'"): # display the SQL queries
        with self.assertNumQueries(3):
            # 1. query: SELECT test, if slug 'foo-bar' exists
            # 2. query: SELECT test, if slug 'foo-bar-2' exists
            # 3. query: INSERT values
            obj = AnotherSlug.objects.create(name=name)
        self.assertEquals(obj.slug, "foo-bar-2")

        #with PrintQueries("create third 'Foo Bar'"): # display the SQL queries
        with self.assertNumQueries(4):
            # 1. query: SELECT test, if slug 'foo-bar' exists
            # 2. query: SELECT test, if slug 'foo-bar-2' exists
            # 3. query: SELECT test, if slug 'foo-bar-3' exists
            # 4. query: INSERT values
            obj = AnotherSlug.objects.create(name=name)
        self.assertEquals(obj.slug, "foo-bar-3")



