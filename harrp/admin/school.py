from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from harrp.models.school import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'city', 'state', ]