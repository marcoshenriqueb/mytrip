from django.contrib import admin
from django import forms
import re
from .models import Service, Faq

class ServiceForm(forms.ModelForm):
    def clean_uri(self):
        if not re.match(r'^[a-z0-9-]+$', self.cleaned_data['uri']):
            raise forms.ValidationError('O endereço ó pode conter letras, números e "-".')
        
        return self.cleaned_data['uri']
        

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)
    form = ServiceForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

@admin.register(Faq)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'created_at', 'updated_at')
    list_display_links = ('question',)
