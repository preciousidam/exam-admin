from others.models.level import Level
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subject(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    icon = models.ImageField(_("Icon"), upload_to='icons', null=True, blank=True)
    level = models.OneToOneField(Level, verbose_name=_("Level"), null=True, blank=True, on_delete=models.SET_NULL, related_name="level")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Topic(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    icon = models.ImageField(_("Icon"), upload_to='icons', null=True, blank=True)
    subject = models.ManyToManyField(Subject, verbose_name=_("Subject"), related_name="topics")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']