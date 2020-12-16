from django.shortcuts import render

from django.views.generic import TemplateView

from pledge.actions import helpers
from pledge.actions.models import Pledge


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_pledges"] = Pledge.objects.all().count
        return context
