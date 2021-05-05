from others.models.level import Level
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subject(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    icon = models.ImageField(_("Icon"), upload_to='icons', null=True, blank=True)
    level = models.ManyToManyField(Level, verbose_name=_("Level"), related_name="subjects")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Topic(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    icon = models.ImageField(_("Icon"), upload_to='icons', null=True, blank=True)
    subject = models.ForeignKey(Subject, verbose_name=_("Subject"), on_delete=models.CASCADE, related_name="topics", null=True, blank=True)
    

    def __str__(self):
        return self.title

    @property
    def subject_title(self) -> str:
        return self.subject.title

    class Meta:
        ordering = ['title']