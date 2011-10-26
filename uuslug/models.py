import os

# create a database table only in unit test mode
if os.environ['DJANGO_SETTINGS_MODULE'] == 'uuslug.testsettings':
    from django.db import models
    from uuslug import uuslug as slugify
    
    class CoolSlug(models.Model):
        name = models.CharField(max_length=100)
        slug = models.CharField(max_length=200)
        
        def __unicode__(self):
            return self.name
        
        def save(self, *args, **kwargs):
            self.slug = slugify(self.name, instance=self)
            super(CoolSlug, self).save(*args, **kwargs)


