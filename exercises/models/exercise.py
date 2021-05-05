from django.db import models
from django.utils.translation import ugettext_lazy as _

from others.models import Topic
# Create your models here.

class Exercise(models.Model):
    TYPE = [('MTC', 'Multichoice'), ('SUB', 'Subjective')]
    topic = models.ForeignKey(Topic, verbose_name=_("Topic"), on_delete=models.SET_NULL, null=True, blank=True, related_name="exercises")
    question = models.TextField(_("Question"))
    image = models.ImageField(_("Image"), upload_to='exercise', null=True, blank=True)
    qtn_type = models.CharField(_("Question Type"), max_length=255, choices=TYPE, default='MTC')
    opt_a = models.CharField(_("Option A"), max_length=255, null=True, blank=True)
    opt_b = models.CharField(_("Option B"), max_length=255, null=True, blank=True)
    opt_c = models.CharField(_("Option C"), max_length=255, null=True, blank=True)
    opt_d = models.CharField(_("Option D"), max_length=255, null=True, blank=True)
    opt_e = models.CharField(_("Option E"), max_length=255, null=True, blank=True)
    answer = models.CharField(_("Answer"), max_length=1024, null=True, blank=True)
    hint = models.CharField(_("Hint"), max_length=255, null=True, blank=True)
    score = models.IntegerField(_("Score"), help_text="How many point question carries")

    def __str__(self) -> str:
        return self.question