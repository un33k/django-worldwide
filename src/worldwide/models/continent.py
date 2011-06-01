# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['Continent']

class Continent(models.Model):
    name = models.CharField(_('Continent name'), max_length=128, unique=True, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)
    code = models.CharField(max_length=2) 
    population = models.PositiveIntegerField(_('Population'), help_text=_('Population'), null=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-continent'
        verbose_name = _('continent')
        verbose_name_plural = _('continents')
        unique_together = (('name','code'), )
        ordering = ('name', 'code', 'slug', 'population',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, instance=self)
        super(Continent, self).save(*args, **kwargs)




