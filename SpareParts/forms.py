from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.models import inlineformset_factory
from .models import *

class SparePartsTypeForm(forms.ModelForm):
    class Meta:
        model = SparePartsTypes
        exclude = ['deleted']

class DeleteTypeForm(forms.ModelForm):
    class Meta:
        exclude = ['name']
        model = SparePartsTypes
        widgets = {

            'deleted': forms.HiddenInput(),
        }
        
class SparePartsNameForm(forms.ModelForm):
    class Meta:
        model = SparePartsNames
        exclude = ['deleted']        
        
        

class DeleteNameForm(forms.ModelForm):
    class Meta:
        exclude = ['name']
        model = SparePartsNames
        widgets = {

            'deleted': forms.HiddenInput(),
        }
                
                
                

class SparePartsWarehouseForm(forms.ModelForm):
    class Meta:
        model = SparePartsWarehouses
        exclude = ['deleted']        
        
        

class WarehouseDeleteForm(forms.ModelForm):
    class Meta:
        exclude = ['name']
        model = SparePartsWarehouses
        widgets = {

            'deleted': forms.HiddenInput(),
        }

class SparePartSupplierForm(forms.ModelForm):
    class Meta:
        model = SparePartsSuppliers
        exclude = ['deleted']        
        
        

class SupplierDeleteForm(forms.ModelForm):
    class Meta:
        exclude = ['name', 'phone', 'initial_balance', 'credit_or_debit']
        model = SparePartsSuppliers
        widgets = {

            'deleted': forms.HiddenInput(),
        }
                                                                