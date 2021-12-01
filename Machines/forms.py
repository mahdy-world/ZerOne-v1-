from django import forms
from .models import *


class MachinesTypesForm(forms.ModelForm):
    class Meta:
        model = MachinesTypes
        exclude = ['deleted']