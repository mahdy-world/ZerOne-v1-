from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models import fields
from django.forms import widgets
from django.forms.models import inlineformset_factory
from .models import *

class SystemInfoForm(forms.ModelForm):
    class Meta:
        model = SystemInformation
        fields = '__all__'