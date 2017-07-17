from django import forms

class LeadForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
