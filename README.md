# Django Uuslug

**A Django slugify application that guarantees `Uniqueness` and handles `Unicode`**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]

# Overview

In short: UUSlug == (`U`nique + `U`nicode) Slug

# How to install

    1. easy_install django-uuslug
    2. pip install django-uuslug
    3. git clone http://github.com/un33k/django-uuslug
        a. cd django-uuslug
        b. run python setup.py
    4. wget https://github.com/un33k/django-uuslug/zipball/master
        a. unzip the downloaded file
        b. cd into django-uuslug-* directory
        c. run python setup.py
    5. pip install -e git+https://github.com/un33k/django-uuslug#egg=django-uuslug

# How to use

```python

 ####### Unicode Test #######

 from uuslug import slugify

 txt = "This is a test ---"
 r = slugify(txt)
 self.assertEqual(r, "this-is-a-test")

 txt = "___This is a test ---"
 r = slugify(txt)
 self.assertEqual(r, "this-is-a-test")

 txt = "___This is a test___"
 r = slugify(txt)
 self.assertEqual(r, "this-is-a-test")

 txt = "This -- is a ## test ---"
 r = slugify(txt)
 self.assertEqual(r, "this-is-a-test")

 txt = '影師嗎'
 r = slugify(txt)
 self.assertEqual(r, "ying-shi-ma")

 txt = 'C\'est déjà l\'été.'
 r = slugify(txt)
 self.assertEqual(r, "c-est-deja-l-ete")

 txt = 'Nín hǎo. Wǒ shì zhōng guó rén'
 r = slugify(txt)
 self.assertEqual(r, "nin-hao-wo-shi-zhong-guo-ren")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt)
 self.assertEqual(r, "jaja-lol-mememeoo-a")

 txt = 'Компьютер'
 r = slugify(txt)
 self.assertEqual(r, "kompiuter")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=9)
 self.assertEqual(r, "jaja-lol")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=15)
 self.assertEqual(r, "jaja-lol-mememe")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=50)
 self.assertEqual(r, "jaja-lol-mememeoo-a")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=15, word_boundary=True)
 self.assertEqual(r, "jaja-lol-a")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=17, word_boundary=True)
 self.assertEqual(r, "jaja-lol-mememeoo")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=18, word_boundary=True)
 self.assertEqual(r, "jaja-lol-mememeoo")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=19, word_boundary=True)
 self.assertEqual(r, "jaja-lol-mememeoo-a")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=20, word_boundary=True, separator=".")
 self.assertEqual(r, "jaja.lol.mememeoo.a")

 txt = 'jaja---lol-méméméoo--a'
 r = slugify(txt, max_length=20, word_boundary=True, separator="ZZZZZZ")
 self.assertEqual(r, "jajaZZZZZZlolZZZZZZmememeooZZZZZZa")

 txt = 'one two three four five'
 r = slugify(txt, max_length=13, word_boundary=True, save_order=True)
 self.assertEqual(r, "one-two-three")

 txt = 'one two three four five'
 r = slugify(txt, max_length=13, word_boundary=True, save_order=False)
 self.assertEqual(r, "one-two-three")

 txt = 'one two three four five'
 r = slugify(txt, max_length=12, word_boundary=True, save_order=False)
 self.assertEqual(r, "one-two-four")

 txt = 'one two three four five'
 r = slugify(txt, max_length=12, word_boundary=True, save_order=True)
 self.assertEqual(r, "one-two")

 txt = 'this has a stopword'
 r = slugify(txt, stopwords=['stopword'])
 self.assertEqual(r, 'this-has-a')

 txt = 'the quick brown fox jumps over the lazy dog'
 r = slugify(txt, stopwords=['the'])
 self.assertEqual(r, 'quick-brown-fox-jumps-over-lazy-dog')

 txt = 'Foo A FOO B foo C'
 r = slugify(txt, stopwords=['foo'])
 self.assertEqual(r, 'a-b-c')

 txt = 'Foo A FOO B foo C'
 r = slugify(txt, stopwords=['FOO'])
 self.assertEqual(r, 'a-b-c')

 txt = 'the quick brown fox jumps over the lazy dog in a hurry'
 r = slugify(txt, stopwords=['the', 'in', 'a', 'hurry'])
 self.assertEqual(r, 'quick-brown-fox-jumps-over-lazy-dog')


 ####### Uniqueness Test #######

 from django.db import models
 from uuslug import uuslug

 # Override your object's save method with something like this (models.py)
 class CoolSlug(models.Model):
     name = models.CharField(max_length=100)
     slug = models.CharField(max_length=200)

     def __unicode__(self):
         return self.name

     def save(self, *args, **kwargs):
         self.slug = uuslug(self.name, instance=self)
         super(CoolSlug, self).save(*args, **kwargs)

 # Note: You can also specify the start number.
 # Example:
     self.slug = uuslug(self.name, instance=self, start_no=2)
     # the second slug should start with "-2" instead of "-1"

 name = "john"
 c = CoolSlug.objects.create(name=name)
 c.save()
 print(c.slug) # => "john"

 c1 = CoolSlug.objects.create(name=name)
 c1.save()
 print(c1.slug) # => "john-1"

 c2 = CoolSlug.objects.create(name=name)
 c2.save()
 print(c2.slug) # => "john-2"


 # If you need truncation of your slug to exact length, here is an example
 class SmartTruncatedSlug(models.Model):
     name = models.CharField(max_length=19)
     slug = models.CharField(max_length=10)

     def __unicode__(self):
         return self.name

     def save(self, *args, **kwargs):
         self.slug = uuslug(self.name, instance=self, max_length=10)
         super(SmartTruncatedSlug, self).save(*args, **kwargs)

 # If you need automatic truncation of your slug, here is an example
 class AutoTruncatedSlug(models.Model):
     name = models.CharField(max_length=19)
     slug = models.CharField(max_length=19)

     def __unicode__(self):
         return self.name

     def save(self, *args, **kwargs):
         self.slug = uuslug(self.name, instance=self)
         super(SmartTruncatedSlug, self).save(*args, **kwargs)
```

# Running the tests

To run the tests against the current environment:

    python manage.py test

# License

Released under a ([BSD](LICENSE.md)) license.

# Version

X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://github.com/un33k/django-uuslug/actions/workflows/main.yml/badge.svg
[status-link]: https://github.com/un33k/django-uuslug/actions/workflows/main.yml
[status-image]: https://github.com/un33k/django-uuslug/actions/workflows/main.yml/badge.svg
[version-image]: https://img.shields.io/pypi/v/django-uuslug.svg
[version-link]: https://pypi.python.org/pypi/django-uuslug
[coverage-image]: https://coveralls.io/repos/un33k/django-uuslug/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-uuslug
[download-image]: https://img.shields.io/pypi/dm/django-uuslug.svg
[download-link]: https://pypi.python.org/pypi/django-uuslug

# Sponsors

[Neekware Inc.](https://github.com/neekware)
