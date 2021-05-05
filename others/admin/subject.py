from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from others.models import Subject, Topic


# Register your models here.


class TopicInlinAdmin(admin.TabularInline):
    model=Topic
    verbose_name=_("Topic")
    verbose_name_plural=_("Topics")
    extra=1


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [TopicInlinAdmin]
    exclude=('subject',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject']