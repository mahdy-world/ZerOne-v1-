from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User

class ChangePasswordForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['password']
        lables = {
            'password': 'كلمة المرور'
        }
        
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', }),
        }

        