from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

# Create your models here.
from others.models import Subject, Topic
from harrp.models import School

class Lesson(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    subject = models.ForeignKey(Subject, verbose_name=_("Subject"), null=True, blank=True, on_delete=models.SET_NULL, related_name="lessons")
    topic = models.ForeignKey(Topic, verbose_name=_("Topic"), null=True, blank=True, on_delete=models.SET_NULL, related_name="lessons")
    feature_image = models.ImageField(_("Featured Image"), upload_to="featured", null=True, blank=True)
    school = models.ForeignKey(School, verbose_name=_("School"), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    heading = models.CharField(_("Heading"), max_length=255, null=True, blank=True)
    body = models.TextField(_("Body"))
    lesson = models.ForeignKey(Lesson, verbose_name=_("Lesson"), on_delete=models.CASCADE, related_name='paragraphs')
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __str__(self):
        return self.heading


class FeaturedImage(models.Model):
    image = models.ImageField(_("Image"), upload_to="featured", null=True, blank=True)
    paragraph = models.ForeignKey(Paragraph, verbose_name=_("Paragraph"), on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Featured Image for {self.paragraph}"
