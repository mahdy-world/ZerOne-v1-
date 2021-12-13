from django import forms
from .models import *

class WorkTreasuryForm(forms.ModelForm):
    class Meta:
        model = WorkTreasury
        exclude = ['deleted']

class WorkTreasuryDeleteForm(forms.ModelForm):
    class Meta:
        exclude = ['name', 'initial_balance']
        model = WorkTreasury
        widgets = {

            'deleted': forms.HiddenInput(),
        }