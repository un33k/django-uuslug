Django Unique-Unicode Slug Application
====================

**A Django slugify application that guarantees uniqueness and handles unicode**

**Author:** Val Neekman, [ info@neekware.com, @vneekman]

Overview
========

A Django slugify application that guarantees uniqueness and handles unicode.
UUSlug == (``U``nique + ``U``nicode) Slug

How to install
==================

    1. easy_install django-uuslug
    2. pip install django-uuslug
    3. git clone http://github.com/un33k/django-uuslug
        a. cd django-uuslug
        b. run python setup.py
    4. wget https://github.com/un33k/django-uuslug/zipball/master
        a. unzip the downloaded file
        b. cd into django-uuslug-* directory
        c. run python setup.py

How to use
=================

Unicode Test

    from uuslug import slugify

    txt = "This is a test ---"
    r = slugify(txt)
    self.assertEquals(r, "this-is-a-test")
    
    txt = "This -- is a ## test ---"
    r = slugify(txt)
    self.assertEquals(r, "this-is-a-test")
    
    txt = 'C\'est déjà l\'été.'
    r = slugify(txt)
    self.assertEquals(r, "cest-deja-lete")

    txt = 'Nín hǎo. Wǒ shì zhōng guó rén'
    r = slugify(txt)
    self.assertEquals(r, "nin-hao-wo-shi-zhong-guo-ren")

    txt = 'Компьютер'
    r = slugify(txt)
    self.assertEquals(r, "kompiuter")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt)
    self.assertEquals(r, "jaja-lol-mememeoo-a")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=9)
    self.assertEquals(r, "jaja-lol")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=15)
    self.assertEquals(r, "jaja-lol-mememe")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=50)
    self.assertEquals(r, "jaja-lol-mememeoo-a")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=15, word_boundary=True)
    self.assertEquals(r, "jaja-lol-a")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=19, word_boundary=True)
    self.assertEquals(r, "jaja-lol-mememeoo")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=20, word_boundary=True)
    self.assertEquals(r, "jaja-lol-mememeoo-a")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=20, word_boundary=True, separator=".")
    self.assertEquals(r, "jaja.lol.mememeoo.a")

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=20, word_boundary=True, separator="ZZZZZZ")
    self.assertEquals(r, "jajaZZZZZZlolZZZZZZmememeooZZZZZZa")

Uniqueness Test

    Override your object's save method with something like this (models.py)

    from django.db import models
    from uuslug import uuslug

    class CoolSlug(models.Model):
        name = models.CharField(max_length=100)
        slug = models.CharField(max_length=200)

        def __unicode__(self):
            return self.name

        def save(self, *args, **kwargs):
            # self.slug = uuslug(self.name, instance=self, separator="_") # optional non-dash separator
            self.slug = uuslug(self.name, instance=self)
            super(CoolSlug, self).save(*args, **kwargs)


    Note: You can also specify the start number.
    Example: 
        self.slug = uuslug(self.name, instance=self, start_no=2)
        # the second slug should start with "-2" instead of "-1"
        
    name = "john"
    c = CoolSlug.objects.create(name=name)
    c.save()
    print c.slug # => "john"

    c1 = CoolSlug.objects.create(name=name)
    c1.save()
    print c1.slug # => "john-1"

    c2 = CoolSlug.objects.create(name=name)
    c2.save()
    print c2.slug # => "john-2"


    # If you need truncation of your slug, here is an example
    class SmartTruncatedSlug(models.Model):
        name = models.CharField(max_length=19)
        slug = models.CharField(max_length=19)

        def __unicode__(self):
            return self.name

        def save(self, *args, **kwargs):
            self.slug = uuslug(self.name, instance=self, start_no=9, max_length=19, word_boundary=True)
            super(SmartTruncatedSlug, self).save(*args, **kwargs)

        # Let's test it
        name = 'jaja---lol-méméméoo--a'

        obj = SmartTruncatedSlug.objects.create(name=name)
        print obj.slug # "jaja-lol-mememeoo"  --- where 19 is max_length (first slug, no duplicate yet)

        obj = SmartTruncatedSlug.objects.create(name=name)
        print obj.slug # "jaja-lol-mememeoo-9" --- where 19 is max_length, start_no = 9

        obj = SmartTruncatedSlug.objects.create(name=name)
        print obj.slug # "jaja-lol-mememeo-10" -- where 19 is max_length, smart appending "-10"


Running the tests
=================

To run the tests against the current environment:

    python manage.py test


Changelog
=========

0.2.0
-----
* Added an option to add a non-dash separator

0.1.0
-----
* Added the ability to truncate slugs + tests (feature request by: Juan Riaza of Spain)

0.9.0
-----
* removed buildout dependency
* splitted unicode slugify into its own python module

0.8
-----
* ORM Optimization & Split of Unicode and Uniqueness into routines (credit: jedie @ github)

0.1 - 0.7
-----
* history file created to track the changes
* singleton "'" handling feature broke the testunit (fix pulled in from re_compile branch)
* re cleanup (pulled in from re_compile branch)
* up the version
* updated the credit section from the README as the referred snippet no longer exists
* include full name in setup.py
* initial release


License
=======

Copyright © Val Neekman.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Note: Django is a registered trademark of the Django Software Foundation.
