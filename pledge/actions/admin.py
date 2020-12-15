from django.contrib import admin

from pledge.actions.models import Action, Constant, Metric


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description", "created", "modified")


@admin.register(Constant)
class ConstantAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "metric",
        "identifier",
        "version",
        "value",
        "created",
        "modified",
    )
    list_filter = ("action", "metric")


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description", "created", "modified")
