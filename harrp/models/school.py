from django.db import models
from django.utils.translation import ugettext_lazy as _

from harrp.constants import  STATE, COUNTRY
from .user import StudentProfile

class School(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    address = models.CharField(_("Address"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=15)
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("State"), max_length=255, choices=STATE)
    country = models.CharField(_("Country"), max_length=50, choices=COUNTRY)
    students = models.ManyToManyField(StudentProfile, verbose_name=_("students"), related_name='schools', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name