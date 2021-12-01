from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import *
from .models import *

# Create your views here.
class SparePartsTypeList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    paginate_by = 10
    

class SparePartsNameList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsNames
    paginate_by = 10
        
    