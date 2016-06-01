from django.db.models.base import ModelBase
from slugify import slugify as pyslugify
from django.utils import six
if six.PY3:
    from django.utils.encoding import smart_str
else:
    from django.utils.encoding import smart_unicode as smart_str

__all__ = ['slugify', 'uuslug']


def slugify(text, entities=True, decimal=True, hexadecimal=True, max_length=0,
            word_boundary=False, separator='-', save_order=False, stopwords=()):
    """
    Make a slug from a given text.
    """

    return smart_str(pyslugify(text, entities, decimal, hexadecimal, max_length,
        word_boundary, separator, save_order, stopwords))


def uuslug(s, instance, entities=True, decimal=True, hexadecimal=True,
           slug_field='slug', filter_dict=None, start_no=1, max_length=0,
           word_boundary=False, separator='-', save_order=False, stopwords=(),
           language_code=None):

    """ This method tries a little harder than django's django.template.defaultfilters.slugify. """

    if isinstance(instance, ModelBase):
        raise Exception("Error: you must pass an instance to uuslug, not a model.")

    queryset = instance.__class__.objects.all()
    if filter_dict:
        queryset = queryset.filter(**filter_dict)
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # The slug max_length cannot be bigger than the max length of the field
    if language_code:
        # To support django parler there's a little more work needed to get the field.
        try:
            meta = instance._parler_meta._get_extension_by_field(slug_field)
            slug_field_max_length = instance._get_translated_model(
                    language_code, meta=meta
                )._meta.get_field(slug_field).max_length
            
        except AttributeError:
            raise Exception("Error: This instance is not from a Django Parler TranslatableModel. Remove language_code parameter and try again.")

    else:
        slug_field_max_length = instance._meta.get_field(slug_field).max_length


    if not max_length or max_length > slug_field_max_length:
        max_length = slug_field_max_length

    slug = slugify(s, entities=entities, decimal=decimal, hexadecimal=hexadecimal,
                   max_length=max_length, word_boundary=word_boundary, separator=separator,
                   save_order=save_order, stopwords=stopwords)

    new_slug = slug
    counter = start_no

    def _new_slug(slug, separator, counter, max_length):
        if len(slug) + len(separator) + len(str(counter)) > max_length:
            slug = slug[:max_length - len(slug) - len(separator) - len(str(counter))]
        return "{}{}{}".format(slug, separator, counter)

    if language_code:
        # need to use translated queryset
        while queryset.translated(**{slug_field: new_slug}):
            new_slug = _new_slug(slug=slug, separator=separator, counter=counter, max_length=max_length)
            counter += 1
    else:
        while queryset.filter(**{slug_field: new_slug}):
            new_slug = _new_slug(slug=slug, separator=separator, counter=counter, max_length=max_length)
            counter += 1

    return new_slug
