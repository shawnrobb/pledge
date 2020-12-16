from django.shortcuts import render

from django.views.generic import TemplateView

from pledge.actions import helpers


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_pledges"] = helpers.get_total_pledges()
        return context
