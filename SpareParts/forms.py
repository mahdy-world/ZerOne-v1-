from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.models import inlineformset_factory
from .models import *

class SparePartsTypeForm(forms.ModelForm):
    class Meta:
        model = SparePartsTypes
        fields = '__all__'
        widgets = {
            'deleted': forms.HiddenInput(),
        }
