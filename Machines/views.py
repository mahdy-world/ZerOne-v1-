from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *


# Create your views here.
class TypesActiveList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesTypes
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'active'
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False)
        return queryset


class TypesTrashList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesTypes
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'trash'
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True)
        return queryset


class TypesCreate(CreateView):
    model = MachinesTypes
    form_class = MachinesTypesForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة مجموعة أصناف رئيسية'
        context['action_url'] = reverse_lazy('Machines:types_create')
        return context

    def get_success_url(self):
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url