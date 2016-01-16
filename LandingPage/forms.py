__author__ = 'varun'

from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)