from django.db import models
from django.utils.translation import ugettext_lazy as _

from .lesson import Lesson
from others.models import Topic
from harrp.models import User

class Note(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"))
    topic = models.ForeignKey(Topic, verbose_name=_("Topic"), on_delete=models.SET_NULL, null=True, blank=True, related_name="%(class)s_notes")
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    

class AdminNote(Note):
    
    class Meta:
        verbose_name_plural = _("Admin Notes")

class StudentNote(Note):
    VISIBILITY = [(0, 'Private'), (1, 'Share with Friends')]
    visibility = models.CharField(_("Visibility"), max_length=50, choices=VISIBILITY, default=0)
    shared = models.ManyToManyField(User, verbose_name=_("Shared With"), related_name="Note")
    user = models.ForeignKey(User, verbose_name=_("Created By"), on_delete=models.CASCADE, related_name='notes', null=True)

    class Meta:
        verbose_name_plural = _("Student Notes")

    @property
    def shared_list(self):
        emails = map(lambda user: user.email, self.shared.all())
        return list(emails)