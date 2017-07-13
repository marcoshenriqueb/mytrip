from django.views.generic.base import TemplateView
from django.views import View
from django.template.response import TemplateResponse
from django.contrib import messages
from django.core.mail import send_mail
from contents.models import Content
from clients.models import Client
from services.models import Service, Faq

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
    def get(self, request, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['service'] = Service.objects.filter(uri=kwargs['uri']).first()
        context['faq'] = Faq.objects.filter(service=context['service'])
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'service.html', context)

    def post(self, request, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['service'] = Service.objects.filter(uri=kwargs['uri']).first()
        context['faq'] = Faq.objects.filter(service=context['service'])
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        form = request.POST
        try:
            send_mail(
                'Contato Site MyView',
                'Serviço: %s,\n\nNome: %s,\nEmail: %s,\nTelefone: %s,\n N de Passageiros: %s,\n Data inicio: %s\
                ,\n Data volta: %s,\n Flexibilidade início: %s,\n Flexibilidade volta: %s\
                ,\n Últimos destinos: %s,\n Viagens Planejadas: %s,\n Preferências: %s\
                ,\n Interesses: %s,\n Restriçoes alimentares: %s,\n Acomodação: %s\
                ,\n Notas gerais: %s,\n Destino: %s,\n Orçamento: %s' % (
                    kwargs['uri'],
                    form['name'],
                    form['email'],
                    form['phone'],
                    form['passengers'],
                    form['startdate'],
                    form['enddate'],
                    form['startrange'],
                    form['endrange'],
                    form['lastdestinations'] or '',
                    form['plannedtrips'] or '',
                    form['preferences'] or '',
                    ', '.join(form.getlist('insterests')) if 'interests' in form else '',
                    form['foodrestrictions'] or '',
                    form['accommodation'] or '',
                    form['notes'] or '',
                    form['whereto'] if 'whereto' in form else '',
                    ', '.join(form.getlist('budget')) if 'budget' in form else '',
                ),
                'myviewsolutions123@gmail.com',
                ['marcoshenriqueb@gmail.com',]
            )
            messages.add_message(request, messages.INFO, 'Obrigado pelo contato, retornaremos em breve!')
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(form['budget'])
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
            context['form'] = form
        return TemplateResponse(request, 'service.html', context)


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
