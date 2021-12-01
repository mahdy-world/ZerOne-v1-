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
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset


class TypesTrashList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesTypes
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'trash'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset


class TypesCreate(CreateView):
    model = MachinesTypes
    form_class = MachinesTypesForm
    success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'create'
        context['action_url'] = reverse_lazy('Machines:types_create')
        return context

    def get_success_url(self):
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url


class TypesUpdate(UpdateView):
    model = MachinesTypes
    form_class = MachinesTypesForm
    success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'update'
        context['action_url'] = reverse_lazy('Machines:types_update', kwargs={'pk': self.object.id})
        return context


class TypesDelete(DeleteView):
    model = MachinesTypes
    form_class = MachinesTypesForm
    success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'delete'
        context['action_url'] = reverse_lazy('Machines:types_delete', kwargs={'pk': self.object.id})
        return context