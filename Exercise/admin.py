from .models import Exercise
from django.contrib import admin


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content')
    list_display_links = ('title',)
    ordering = ('ex_id',)