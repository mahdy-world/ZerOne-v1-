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
                                                                
class SparePartOrderForm(forms.ModelForm):
    class Meta:
        model = SparePartsOrders
        exclude = ['deleted']
        widgets = {
            'order_supplier':forms.Select(attrs={'class':'form-control'}),
            'order_deposit_value':forms.NumberInput(attrs={'class':'form-control'}),
            'order_number':forms.TextInput(attrs={'class':'form-control'}),
            'order_date' :forms.DateInput(attrs={'type': 'date','class':'form-control' }),
            'order_deposit_date' :forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'order_rest_date' :forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'order_receipt_date' :forms.DateInput(attrs={'type': 'date','class':'form-control'}),
        }        
        
        

class OrderDeleteForm(forms.ModelForm):
    class Meta:
        exclude = ['order_number', 'order_date', 'order_supplier', 'order_deposit_value', 'order_deposit_date', 'order_rest_date', 'order_receipt_date']
        model = SparePartsOrders
        widgets = {

            'deleted': forms.HiddenInput(),
        }


class orderProductForm(forms.ModelForm):
    class Meta:
        model = SparePartsOrderProducts
        fields = ['product_name','product_quantity', 'product_price']
        widgets = {

            'product_name':forms.Select(attrs={'class':'form-control' , 'id':'product' }),
            'product_quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'product_price' :forms.NumberInput(attrs={'class':'form-control' }),
            
        }        
        
        
                                                                        