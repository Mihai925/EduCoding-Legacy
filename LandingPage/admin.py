from django.contrib import admin
from .models import Feature, LandingPage


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    ordering = ('description',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon',)
    ordering = ('title',)