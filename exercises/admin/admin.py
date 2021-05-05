from django.contrib import admin

from exercises.models import Exercise

# Register your models here.

@admin.register(Exercise)
class ExerciseAdminView(admin.ModelAdmin):
    list_display = ['question', 'topic', 'qtn_type', 'answer', 'opt_a', 'opt_b', 'opt_c', 'opt_d', 'opt_e', 'hint']