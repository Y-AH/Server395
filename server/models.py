from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __unicode__(self):
        return "{} {}".format(self.name, self.phone)

