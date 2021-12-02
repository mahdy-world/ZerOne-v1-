from django import forms
from .models import *


class MachinesTypesForm(forms.ModelForm):
    class Meta:
        model = MachinesTypes
        exclude = ['deleted']


class MachinesTypesFormDelete(forms.ModelForm):
    class Meta:
        model = MachinesTypes
        exclude = ['name']
        widgets = {
            'deleted': forms.HiddenInput(),
        }