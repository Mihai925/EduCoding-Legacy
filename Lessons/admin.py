from .models import Lesson, Unit
from django.contrib import admin


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'briefing', 'introduction')
    list_editable = ()
    ordering = ('lesson_id',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_id')
    list_editable = ('title', )
    ordering = ('unit_id', )