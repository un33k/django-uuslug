# -*- coding: utf-8 -*-

__version__ = '0.9.0'

from django.utils.encoding import smart_unicode
from slugify import slugify as pyslugify

__all__ = ['slugify', 'uuslug']

def slugify(text, entities=True, decimal=True, hexadecimal=True):
    """ Make a slug from a given text """
    
    return smart_unicode(pyslugify(text, entities, decimal, hexadecimal))


def uuslug(s, instance, entities=True, decimal=True, hexadecimal=True,
    slug_field='slug', filter_dict=None, start_no=1):
    """This method tries a little harder than django's django.template.defaultfilters.slugify.

    Parameters
    ----------
    s : string
        Explanation
    entities: boolean, optional
        Explanation
    decimal : boolean, optional
        Explanation
    hexadecimal : boolean, optional
        Explanation
    instance : Model object or None, optional
        Explanation
    slug_field : string, optional
        Explanation
    filter_dict : dictionary, optional
        Explanation

    Returns
    -------
    slug : string
        Explanation

    Examples
    --------
    Example usage in save method for model:
    
    import uuslug as slugify
    self.slug = slugify(self.name, instance=self)
    """
    if hasattr(instance, 'objects'):
        raise Exception("Error: you must pass an instance to uuslug, not a model.")

    queryset = instance.__class__.objects.all()
    if filter_dict:
        queryset = queryset.filter(**filter_dict)
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    slug1 = slugify(s, entities=entities, decimal=decimal, hexadecimal=hexadecimal)
    slug2 = slug1

    counter = start_no
    while queryset.filter(**{slug_field: slug2}).exists():
        slug2 = "%s-%s" % (slug1, counter)
        counter += 1

    return slug2
