from django.contrib import admin
from .models import Feature, LandingPage, Quotes


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    ordering = ('description',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon',)
    ordering = ('title',)

admin.site.register(Quotes)