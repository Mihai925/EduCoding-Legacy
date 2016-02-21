from django.utils.translation import ugettext as _
from django import forms


class TeacherRegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your Name')}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your Surname')}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your Email')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Enter Password')}))
