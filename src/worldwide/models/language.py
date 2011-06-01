# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uslug import uSlug as slugify

__all__ = ['Language']

class Language(models.Model):
    name = models.CharField(_('Language'), max_length=128, db_index=True, blank=False, null=False)
    slug = models.CharField(_('Slug'), max_length=128, db_index=True)
    percent = models.FloatField(_('Worldwide Percentage'), blank=True, null=True)
    dialect = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label = 'worldwide'
        db_table = app_label + '-language'
        verbose_name = _('language')
        verbose_name_plural = _('languages')
        ordering = ('name', 'dialect', 'slug', 'percent',)

    def save(self, *args, **kwargs):
        s = self.name
        if self.dialect:
            s += '-' + self.dialect
        self.slug = slugify(self.name, instance=self)
        super(Language, self).save(*args, **kwargs)



