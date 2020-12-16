from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from pledge.actions import helpers
from pledge.actions.models import Metric, Pledge


User = get_user_model()


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
        context["users"] = User.objects.exclude(id=self.request.user.id)
        context["my_pledges"] = Pledge.objects.filter(user=self.request.user)
        return context


class UserPledgesView(DetailView):
    """View to display the Pledges a user has made."""

    template_name = "actions/user_pledges.html"
    model = User

    def get_object(self):
        return get_object_or_404(self.model, username=self.kwargs["username"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pledges"] = Pledge.objects.filter(user=self.get_object())
        return context
