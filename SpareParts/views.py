
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import *

from .forms import SparePartsTypeForm
from .models import *

# Create your views here.
class SparePartsTypeList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    paginate_by = 10
    template_name = 'SpareParts/sparepartstypes_list'

class SparePartsTypeCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    form_class = SparePartsTypeForm
    template_name = 'SpareParts/form.html'
    success_url = reverse_lazy('SpareParts:SpareTypeList')

    


    