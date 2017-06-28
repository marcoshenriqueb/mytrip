from django.views.generic.base import TemplateView
from contents.models import Content
from clients.models import Client
from services.models import Service

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['services'] = Service.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context


class ServicePageView(TemplateView):
    template_name = "service.html"

    def get_context_data(self, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['service'] = Service.objects.filter(uri=kwargs['uri']).first()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context


class CorporateView(TemplateView):
    template_name = "corp.html"

    def get_context_data(self, **kwargs):
        context = super(CorporateView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context
