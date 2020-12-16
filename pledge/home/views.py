from django.shortcuts import render

from django.views.generic import TemplateView

from pledge.actions import helpers
from pledge.actions.models import Metric, Pledge


class HomeView(TemplateView):
    """View that handles displaying the home page with summary data."""

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_pledges"] = Pledge.objects.all().count
        # add summary data for applicable metrics to context
        metrics = []
        for metric in Metric.objects.all():
            metrics.append((metric.title, helpers.get_total_impact(metric)))
        context["metrics"] = metrics
        return context
