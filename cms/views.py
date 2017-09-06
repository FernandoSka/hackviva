"""CMS Views."""
from django.views.generic import (
    TemplateView,
)


class HomeView(TemplateView):
    """View that shows the first page of the web app."""

    template_name = 'home.html'
