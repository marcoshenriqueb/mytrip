from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    uri = models.CharField("Endereço", max_length=255, unique=True, null=True)
    description = models.TextField("Descrição", null=True, blank=True)
    description_home = models.TextField("Descrição home", null=True, blank=True)
    icon = models.ImageField("Ícone", upload_to='servicesicons/%Y/%m/%d/', max_length=255, null=True, blank=True)
    photo = models.ImageField("Foto", upload_to='servicesphotos/%Y/%m/%d/', max_length=255, null=True, blank=True)
    photo_position = models.CharField("Posição da foto", max_length=15, null=True, blank=True)
    form = models.IntegerField("Form (não mudar)", null=True, blank=True, unique=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.name

class Faq(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name="Serviço")
    question = models.TextField("Pergunta", null=False, blank=False)
    answer = models.TextField("Resposta", null=False, blank=False)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return self.question
