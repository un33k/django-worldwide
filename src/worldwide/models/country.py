# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['Country']

class Country(models.Model):
    name = models.CharField(_('Country name'), max_length=128, unique=True, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)
    full_name = models.CharField(_('Official country name'), max_length=128)
    capital = models.ForeignKey('City', null=True, related_name="country_capital")   
    iso_2 = models.CharField(_('ISO alpha-2'), max_length=2, null=True, primary_key=True)
    iso_3 = models.CharField(_('ISO alpha-3'), max_length=3, null=True)
    iso_code = models.PositiveSmallIntegerField(_('ISO numeric'), null=True)
    idc = models.PositiveIntegerField(_('Iternational Dialing Code'), null=True)
    tld = models.CharField(_('Top Level Domain code'), max_length=7, null=True)
    currency = models.ForeignKey('Currency', help_text=_('Currency'), null=True)
    latitude = models.FloatField(_('Latitude'), blank=True, null=True)
    longitude = models.FloatField(_('Longitude'), blank=True, null=True)
    population = models.PositiveIntegerField(_('Population'), help_text=_('Population'), null=True)
    continent = models.ForeignKey('Continent', help_text=_('Continent'), null=True)
    jurisdiction = models.ForeignKey('self', help_text=_('Sovereignty'), null=True)
    neighbours = models.ManyToManyField('self', help_text=_('Neighbouring Countries'), null=True)
    languages = models.ManyToManyField('Language', help_text=_('Language'), null=True)    
    area = models.PositiveIntegerField(_('Area - Square Meters'), null=True)
    time_zone = models.CharField(_('Standard time zone (UTC/GMT)'), max_length=20, null=True) 
    tmz_abbr = models.CharField(_('Time zone abbreviation'), max_length=5, null=True)
    active = models.BooleanField(_('Active'), default=False)
            
    def __unicode__(self):
        return self.full_name

    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-country'
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ('name', 'full_name', 'iso_2',)

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.name
        self.slug = slugify(self.name, instance=self)
        super(Country, self).save(*args, **kwargs)







