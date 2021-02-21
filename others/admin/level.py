from django.contrib import admin

from others.models import Level


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass