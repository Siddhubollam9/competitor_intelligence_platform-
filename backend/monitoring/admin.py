from django.contrib import admin
from .models import Competitor, ScrapedUpdate


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "created_at")


@admin.register(ScrapedUpdate)
class ScrapedUpdateAdmin(admin.ModelAdmin):
    list_display = ("competitor", "title", "collected_at")