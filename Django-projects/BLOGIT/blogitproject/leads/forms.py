from django import forms
from leads.models import Lead

class LeadForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        }
    ))
    subject = forms.CharField(widget=forms.TextInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Enter Subject',
       } 
    ))
    email = forms.EmailField(widget=forms.TextInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Your Email',
           'type': 'Enter your email',
       } 
    ))
    message = forms.CharField(widget=forms.Textarea(
       attrs={
           'class': 'form-control w-100',
           'placeholder': 'Enter Message',
       } 
    ))

    class Meta:
        model = Lead
        fields = ['name', 'subject', 'email', 'message']