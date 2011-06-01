# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['County']

class County(models.Model):
    name = models.CharField(_('County name'), max_length=128, unique=True, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-county'
        verbose_name = _('county')
        verbose_name_plural = _('counties')
        ordering = ('name', 'slug',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, instance=self)
        super(County, self).save(*args, **kwargs)




