from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import nested_admin

from lessons.models import Paragraph, Lesson, FeaturedImage


# Register your models here.

class FeaturedImageInline(nested_admin.NestedTabularInline):
    extra=1
    model=FeaturedImage
    verbose_name_plural=_("Featured Images")
    verbose_name=_("Image")
    

class ParagraphInline(nested_admin.NestedStackedInline):
    model=Paragraph
    extra=1
    verbose_name_plural=_("Body")
    verbose_name=_("Paragraph")
    inlines=[FeaturedImageInline]


@admin.register(Lesson)
class LessonAdmin(nested_admin.NestedModelAdmin):
    inlines=[ParagraphInline]
    list_display=['title', 'subject', 'topic', 'created_at', 'last_modified']