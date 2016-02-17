__author__ = 'varun'

from django import forms


class TeacherRegistrationForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeatPassword = forms.CharField(widget=forms.PasswordInput())
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()
