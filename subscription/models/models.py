from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date, timedelta, datetime, timezone

from harrp.models import User

# Create your models here.

class Plan(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    price = models.FloatField(_("Price"))
    duration = models.IntegerField(_("Duration"), help_text="Number of months. Accpted inputs are (1 or 2 or 3 etc")
    discount = models.FloatField(_("Discount"), default=0, help_text="Accpted inputs are (0 to 1", null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} ({self.price})'
    
    class Meta:
        ordering = ['price']


class Subscription(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True, blank=True)
    plan = models.ForeignKey(Plan, verbose_name=_("Plan"), on_delete=models.SET_NULL, null=True, blank=True)
    pay_ref = models.CharField(_("Pay Reference"), max_length=255)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __str__(self) -> str:
        return f'{self.pay_ref}'

    @property
    def active(self):
        expiry_date = self.created_at + timedelta(days=(self.plan.duration * 30))
        diff = expiry_date - datetime.now(timezone.utc)
        return diff.days > 0

    class Meta:
        ordering = ['-last_modified']