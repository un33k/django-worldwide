# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['Ocean']

class Ocean(models.Model):
    name = models.CharField(_('Ocean name'), max_length=128, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)
    area = models.PositiveIntegerField(_('Area - Square Meters'), null=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-ocean'
        verbose_name = _('ocean')
        verbose_name_plural = _('oceans')
        ordering = ('name', 'slug', 'area',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, instance=self)
        super(Ocean, self).save(*args, **kwargs)



