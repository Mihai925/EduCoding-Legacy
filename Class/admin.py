from django.contrib import admin
from .models import Class, Invitation


@admin.register(Class)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('cls_id', 'description', 'name')
    list_editable = ('description', 'name' )
    ordering = ('cls_id',)


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'invitation_code', 'student_email', 'created_date')
    ordering = ('teacher', 'student_email', )

