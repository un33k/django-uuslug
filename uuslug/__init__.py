# -*- coding: utf-8 -*-

__version__ = '0.1.1'

from django.utils.encoding import smart_unicode
from slugify import slugify as pyslugify

__all__ = ['slugify', 'uuslug']

def slugify(text, entities=True, decimal=True, hexadecimal=True, max_length=0, word_boundary=False):
    """ Make a slug from a given text """
    
    return smart_unicode(pyslugify(text, entities, decimal, hexadecimal, max_length, word_boundary))


def uuslug(s, instance, entities=True, decimal=True, hexadecimal=True,
    slug_field='slug', filter_dict=None, start_no=1, max_length=0, word_boundary=False):

    """ This method tries a little harder than django's django.template.defaultfilters.slugify. """

    if hasattr(instance, 'objects'):
        raise Exception("Error: you must pass an instance to uuslug, not a model.")

    queryset = instance.__class__.objects.all()
    if filter_dict:
        queryset = queryset.filter(**filter_dict)
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    slug = slugify(s, entities=entities, decimal=decimal, hexadecimal=hexadecimal, max_length=max_length, word_boundary=word_boundary)

    new_slug = slug
    counter = start_no
    while queryset.filter(**{slug_field: new_slug}).exists():
        if max_length > 0:
            if len(slug) + len('-') + len(str(counter)) > max_length:
                slug = slug[:max_length-len(slug)-len('-')-len(str(counter))] # make room for the "-1, -2 ... etc"
        new_slug = "%s-%s" % (slug, counter)
        counter += 1

    return new_slug





