__author__ = 'varun'

from django import forms
from django_ace import AceWidget


class ExerciseForm(forms.Form):
    code = forms.CharField(widget=AceWidget(mode='python', theme="github", height="440px", wordwrap=True))


class NewExerciseForm(forms.Form):
    code = forms.CharField(widget=AceWidget(mode='python', theme="github", height="440px", width="100%", wordwrap=True))
    inputTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Title"}))
    inputDescription = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Describe the exercise..."}))
    language = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[("Python", "Python")])
    add_tests = forms.BooleanField()