__author__ = 'varun'

from django import forms
from .lookups import UserLookup
import selectable.forms as selectable


class AddStudentForm(forms.Form):
    student = forms.CharField(
        label='Type the email of a student',
        widget=selectable.AutoCompleteWidget(UserLookup),
        required=False,
    )