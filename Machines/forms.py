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


#######################################################


class MachinesWarehousesForm(forms.ModelForm):
    class Meta:
        model = MachinesWarehouses
        exclude = ['deleted']


class MachinesWarehousesFormDelete(forms.ModelForm):
    class Meta:
        model = MachinesWarehouses
        exclude = ['name']
        widgets = {
            'deleted': forms.HiddenInput(),
        }


#######################################################


class MachinesNamesForm(forms.ModelForm):
    class Meta:
        model = MachinesNames
        exclude = ['deleted']


class MachinesNamesFormDelete(forms.ModelForm):
    class Meta:
        model = MachinesNames
        exclude = ['name']
        widgets = {
            'deleted': forms.HiddenInput(),
        }


#######################################################


class MachinesSuppliersForm(forms.ModelForm):
    class Meta:
        model = MachinesSuppliers
        exclude = ['deleted']


class MachinesSuppliersFormDelete(forms.ModelForm):
    class Meta:
        model = MachinesSuppliers
        exclude = ['name', 'phone', 'initial_balance', 'credit_or_debit']
        widgets = {
            'deleted': forms.HiddenInput(),
        }