# -*- coding: utf-8 -*-
import os
import pkg_resources

try:
    _s = os.environ['DJANGO_SETTINGS_MODULE']
except KeyError:
    # DJANGO_SETTINGS_MODULE should have been set by now, if not, we must be in test mode
    os.environ['DJANGO_SETTINGS_MODULE'] = 'uuslug.testsettings'

import re
import unicodedata
from htmlentitydefs import name2codepoint
from django.utils.encoding import smart_unicode, force_unicode
from types import UnicodeType

pkg_resources.require("Unidecode")
from unidecode import unidecode

# only allow the import of our public APIs (UU-SLUG = Uniqure & Unicode Slug)
__all__ = ['uuslug']


# character entity reference
CHAR_ENTITY_REXP = re.compile('&(%s);' % '|'.join(name2codepoint))

# decimal character reference
DECIMAL_REXP = re.compile('&#(\d+);')

# hexadecimal character reference
HEX_REXP = re.compile('&#x([\da-fA-F]+);')

REPLACE1_REXP = re.compile(r'[\']+')
REPLACE2_REXP = re.compile(r'[^-a-z0-9]+')
REMOVE_REXP = re.compile('-{2,}')


def uuslug(s, entities=True, decimal=True, hexadecimal=True,
   instance=None, slug_field='slug', filter_dict=None):
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

    if type(s) != UnicodeType:
        s = unicode(s, 'utf-8', 'ignore')

    # decode now ( 影師嗎 = Ying Shi Ma)
    s = unidecode(s)

    s = smart_unicode(s)

    #character entity reference
    if entities:
        s = CHAR_ENTITY_REXP.sub(lambda m: unichr(name2codepoint[m.group(1)]), s)

    #decimal character reference
    if decimal:
        try:
            s = DECIMAL_REXP.sub(lambda m: unichr(int(m.group(1))), s)
        except:
            pass

    #hexadecimal character reference
    if hexadecimal:
        try:
            s = HEX_REXP.sub(lambda m: unichr(int(m.group(1), 16)), s)
        except:
            pass

    #translate
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

    #replace unwanted characters
    s = REPLACE1_REXP.sub('', s.lower()) # replace ' with nothing instead with -
    s = REPLACE2_REXP.sub('-', s.lower())

    #remove redundant -
    s = REMOVE_REXP.sub('-', s).strip('-')

    slug = s
    if instance:
        def get_query():
            if hasattr(instance, 'objects'):
                raise Exception("Error: you must pass an instance to uuslug, not a model.")
            query = instance.__class__.objects.filter(**{slug_field: slug})
            if filter_dict:
                query = query.filter(**filter_dict)
            if instance.pk:
                query = query.exclude(pk=instance.pk)
            return query
        counter = 1
        while get_query():
            slug = "%s-%s" % (s, counter)
            counter += 1
    return slug
