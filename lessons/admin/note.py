from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from lessons.models import AdminNote, StudentNote


@admin.register(AdminNote)
class AdminNoteAdmin(admin.ModelAdmin):
    pass

@admin.register(StudentNote)
class StudentNoteAdmin(admin.ModelAdmin):
    pass