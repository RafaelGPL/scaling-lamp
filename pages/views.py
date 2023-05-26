from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class MissionPageView(TemplateView):
    template_name = "pages/mission.html"

class CarerPageView(TemplateView):
    template_name = "pages/careers.html"
