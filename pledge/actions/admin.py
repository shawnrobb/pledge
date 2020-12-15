from django.contrib import admin

from pledge.actions.models import (
    Action,
    Constant,
    Metric,
    Pledge,
    Question,
    SelectOption,
    Formula,
)


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


@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "action",
        "attribute",
        "value",
        "created",
        "modified",
    )
    list_filter = ("action",)


class SelectOptionInline(admin.TabularInline):
    model = SelectOption


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("action", "identifier", "question_type")
    list_filter = ("action", "question_type")
    inlines = [SelectOptionInline]


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "metric",
        "version",
        "eval_string",
        "created",
        "modified",
    )
    list_filter = ("action", "metric")