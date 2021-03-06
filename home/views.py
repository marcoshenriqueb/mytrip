from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from contents.models import Content
from clients.models import Client
from services.models import Service, Faq
from .forms import LeadForm

emails = [
    # 'marcoshenriqueb@gmail.com',
    'contato@mytripviagens.com',
    'mytrip@solid.com.br',
]

from_email = 'MyTrip by Solid <myviewsolutions123@gmail.com>'

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

class LeadView(View):
    def post(self, request):
        try:
            form = LeadForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Seu email foi adicionado a nossa newsletter!')
                send_mail(
                    'MyTrip by Solid - Entrada para lead de mailing',
                    form.cleaned_data['email'],
                    from_email,
                    emails
                )
            else:
                messages.add_message(request, messages.INFO, 'Digite um email válido, por favor.')
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos adicionar o email na newsletter, por favor tente novamente.')
        return HttpResponseRedirect(reverse('home') + '#contact')


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
            if context['service'].form == 1:
                send_mail(
                    'MyTrip by Solid - Surpresa',
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
                    from_email,
                    emails
                )
            if context['service'].form == 2:
                send_mail(
                    'MyTrip by Solid - Do seu jeito',
                    'Serviço: %s,\n\nNome: %s,\nEmail: %s,\nTelefone: %s,\n N de Passageiros: %s,\
                    \n Origem: %s,\n Destinos: %s,\n Data inicio: %s\
                    ,\n Data volta: %s,\n Flexibilidade início: %s,\n Flexibilidade volta: %s\
                    ,\n Observações: %s,\n Passagem: %s,\n Hotel: %s\
                    ,\n Tipo de experiência: %s,\n Obs serviço de viagem: %s,\n Obs roteiro personalizado e experiência completa: %s\
                    ,\n Preferência de hotel ou cia aérea: %s,\n Viaja com animais: %s,\n Necessidades especiais: %s\
                    ,\n Restrição alimentar: %s' % (
                        kwargs['uri'],
                        form['name'],
                        form['email'],
                        form['phone'],
                        form['passengers'],
                        form['origin'],
                        form['destination'],
                        form['startdate'],
                        form['enddate'],
                        form['startrange'],
                        form['endrange'],
                        form['notes'] or '',
                        form['ticket'] or '',
                        form['hotel'] or '',
                        form['experience'] if 'experience' in form else '',
                        ', '.join(form.getlist('experiencedetail')) if 'experiencedetail' in form else '',
                        form['experiencedetail2'] or '',
                        form['preferences'] or '',
                        form['animals'] or '',
                        form['special'] or '',
                        form['food'] or ''
                    ),
                    from_email,
                    emails
                )
            if context['service'].form == 3:
                send_mail(
                    'MyTrip by Solid - Destination Wedding',
                    'Nome: %s,\nEmail: %s,\nTelefone: %s,\n Mensagem: %s' % (
                        form['name'],
                        form['email'],
                        form['phone'],
                        form['message'],
                    ),
                    from_email,
                    emails
                )
            messages.add_message(request, messages.INFO, 'Obrigado pelo contato, retornaremos em breve!')
        except Exception as e:
            # import logging
            # logger = logging.getLogger(__name__)
            # logger.error(e)
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
            context['form'] = form
        return TemplateResponse(request, 'service.html', context)


class CorporateView(TemplateView):
    def get(self, request, **kwargs):
        context = super(CorporateView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'corp.html', context)

    def post(self, request, **kwargs):
        context = super(CorporateView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        form = request.POST
        try:
            send_mail(
                'MyTrip by Solid - Corporate',
                'Nome: %s,\nEmail: %s,\nTelefone: %s,\n Mensagem: %s' % (
                    form['name'],
                    form['email'],
                    form['phone'],
                    form['message'],
                ),
                from_email,
                emails
            )
            messages.add_message(request, messages.INFO, 'Obrigado pelo contato, retornaremos em breve!')
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(e)
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
            context['form'] = form
        return TemplateResponse(request, 'corp.html', context)
