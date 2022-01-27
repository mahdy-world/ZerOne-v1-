from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date', 'customer', 'warehouse', 'treasury']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceSpareForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date', 'customer', 'warehouse_spare', 'treasury']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceForm2(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date', 'customer', 'treasury']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceSaveForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['total', 'discount', 'overall', 'comment']
        widgets = {
            'total': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inv_total', 'readonly': 'readonly'}),
            'overall': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inv_overall', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discount'].widget.attrs = {'min': '0', 'max': self['total'].value(), 'id': 'inv_discount'}


class InvoiceBackForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['saved']
        widgets = {
            'saved': forms.HiddenInput(),
        }


class InvoicePayForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['overall', 'paid_value', 'residual_value', 'residual_value_pay_date']
        widgets = {
            'residual_value_pay_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'inv_pay_residual_value_pay_date'}),
            'overall': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inv_pay_overall', 'readonly': 'readonly'}),
            'residual_value': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inv_pay_residual_value', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paid_value'].widget.attrs = {'min': '0', 'max': self['overall'].value(), 'id': 'inv_pay_paid_value'}
        self.fields['residual_value_pay_date'].required = False


class InvoiceOutForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['out_of_warehouse']
        widgets = {
            'out_of_warehouse': forms.HiddenInput(),
        }


class InvoiceDeleteForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['deleted']
        widgets = {
            'deleted': forms.HiddenInput(),
        }


class MachinesInvoiceProductsForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['item', 'unit_price', 'quantity', 'total_price']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control', 'id': 'item'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'unit_price'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'total_price', 'readonly': 'readonly'}),
        }


class MachinesInvoiceSpareProductsForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['item_spare', 'unit_price', 'quantity', 'total_price']
        widgets = {
            'item_spare': forms.Select(attrs={'class': 'form-control', 'id': 'item'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'unit_price'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'total_price', 'readonly': 'readonly'}),
        }


class MachinesInvoiceProductsFormUpdate(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['item', 'unit_price', 'quantity', 'total_price']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control', 'id': 'item', 'readonly': 'readonly'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'unit_price'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'total_price', 'readonly': 'readonly'}),
        }


class MachinesInvoiceSpareProductsFormUpdate(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['item_spare', 'unit_price', 'quantity', 'total_price']
        widgets = {
            'item_spare': forms.Select(attrs={'class': 'form-control', 'id': 'item', 'readonly': 'readonly'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'unit_price'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'total_price', 'readonly': 'readonly'}),
        }


class MachinesInvoiceProductsDeleteForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['deleted']
        widgets = {
            'deleted': forms.HiddenInput(),
        }