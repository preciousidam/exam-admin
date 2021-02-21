from django.db import models
from django.utils.translation import ugettext_lazy as _

from harrp.constants  import LEVEL

class Level(models.Model):
    title= models.CharField(_("Title"), max_length=50, choices=LEVEL)

    def __str__(self):
        return self.title