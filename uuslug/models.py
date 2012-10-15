import os

# create a database table only in unit test mode
if 'testsettings' in os.environ['DJANGO_SETTINGS_MODULE']:
    from django.db import models
    from uuslug import uuslug

    class CoolSlug(models.Model):
        name = models.CharField(max_length=100)
        slug = models.CharField(max_length=200)

        def __unicode__(self):
            return self.name

        def save(self, *args, **kwargs):
            self.slug = uuslug(self.name, instance=self)
            super(CoolSlug, self).save(*args, **kwargs)


    class AnotherSlug(models.Model):
        name = models.CharField(max_length=100)
        slug = models.CharField(max_length=200)

        def __unicode__(self):
            return self.name

        def save(self, *args, **kwargs):
            self.slug = uuslug(self.name, instance=self, start_no=2)
            super(AnotherSlug, self).save(*args, **kwargs)


