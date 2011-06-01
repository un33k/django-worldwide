# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['City']

class City(models.Model):
    name = models.CharField(_('City name'), max_length=128, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)
    state = models.ForeignKey('State', related_name="city_state", null=True)
    country = models.ForeignKey('Country', related_name="city_country", null=True)
    county = models.ForeignKey('County', null=True)
    sister = models.ManyToManyField('self', help_text=_('Sister Cities, if this is a capital city'), blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(_('Latitude'), blank=True, null=True)
    longitude = models.FloatField(_('Longitude'), blank=True, null=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-city'
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        unique_together = (("name", "state", "country"),)

    def save(self, *args, **kwargs):
        s = self.name
        if self.state:
            s += '-' + self.state.name
        if self.country:
            s += '-' + self.country.name
        self.slug = slugify(s, instance=self)
        super(City, self).save(*args, **kwargs)



