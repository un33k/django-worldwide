# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['State']

STATE_CHOICES = (
    ('Province', 'Province'),
    ('State', 'State'),
    ('Department', 'Department'),
    ('Territory', 'Territory'),
    ('Ostan', 'Ostan'),
)

class State(models.Model):
    name = models.CharField(_('State name'), max_length=128, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)
    capital = models.ForeignKey('City', related_name="state_capital", null=True)
    country = models.ForeignKey('Country', related_name="state_country", null=True)
    latitude = models.FloatField(_('Latitude'), blank=True, null=True)
    longitude = models.FloatField(_('Longitude'), blank=True, null=True)
    state_type = models.CharField(max_length =128, blank=True, null=True, choices=STATE_CHOICES)
    population = models.PositiveIntegerField(_('Population'), help_text=_('Population'), null=True)
    code = models.CharField(max_length=2)

    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-state'
        verbose_name = _('state')
        verbose_name_plural = _('states')
        unique_together = (("name", "country"),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, instance=self)
        super(State, self).save(*args, **kwargs)



