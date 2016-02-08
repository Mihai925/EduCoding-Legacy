from django.contrib import admin
from .models import Class


@admin.register(Class)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('cls_id', 'description', 'name')
    list_editable = ('description', 'name' )
    ordering = ('cls_id',)




