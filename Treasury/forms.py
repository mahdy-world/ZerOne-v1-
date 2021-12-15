from django import forms
from .models import *

class WorkTreasuryForm(forms.ModelForm):
    class Meta:
        model = WorkTreasury
        exclude = ['deleted']

class WorkTreasuryDeleteForm(forms.ModelForm):
    class Meta:
        exclude = ['name', 'balance']
        model = WorkTreasury
        widgets = {

            'deleted': forms.HiddenInput(),
        }


class HomeTreasuryForm(forms.ModelForm):
    class Meta:
        model = HomeTreasury
        exclude = ['deleted']

class HomeTreasuryDeleteForm(forms.ModelForm):
    class Meta:
        exclude = ['name', 'balance']
        model = HomeTreasury
        widgets = {

            'deleted': forms.HiddenInput(),
        }
        
        
        
        
class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        exclude = ['deleted']

class BankAccountDeleteForm(forms.ModelForm):
    class Meta:
        exclude = ['name', 'balance','account_no']
        model = BankAccount
        widgets = {

            'deleted': forms.HiddenInput(),
        }