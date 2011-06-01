# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['Currency']

class Currency(models.Model):
    name = models.CharField(_('Currency name'), max_length=128, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)
    code = models.CharField(max_length=5) 
        
    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-currency'
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')
        unique_together = (('name','code'), )
        ordering = ('name', 'code', 'slug',)

    def save(self, *args, **kwargs):
        s = self.name
        if self.code:
            s += '-' + self.code
        self.slug = slugify(self.name, instance=self)
        super(Currency, self).save(*args, **kwargs)



