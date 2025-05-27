# Register your models here.
from django.contrib import admin

from .models import Environment, Evaluation, FeatureFlag, Organisation, Project


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "owner__username")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "organisation", "api_key")
    search_fields = ("name", "organisation__name", "api_key")
    list_filter = ("organisation",)


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ("name", "project")
    list_filter = ("project__organisation", "project")


@admin.register(FeatureFlag)
class FeatureFlagAdmin(admin.ModelAdmin):
    list_display = ("key", "environment", "enabled", "percentage", "updated_at")
    list_filter = ("environment__project__organisation", "environment")
    search_fields = ("key",)


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("flag", "user_identifier", "result", "created_at")
    list_filter = ("flag__environment__project__organisation", "result")
    readonly_fields = ("created_at",)
