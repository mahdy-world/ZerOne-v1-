from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
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
        context['message'] = 'active'
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
        context['message'] = 'trash'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset


class TypesCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = MachinesTypes
    form_class = MachinesTypesForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة نوع ماكينة '
        context['message'] = 'create'
        context['action_url'] = reverse_lazy('Machines:types_create')
        return context

    # def get_success_url(self):
    #     if self.request.POST.get('url'):
    #         return self.request.POST.get('url')
    #     else:
    #         return self.success_url


class TypesUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesTypes
    form_class = MachinesTypesForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل نوع ماكينة: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Machines:types_update', kwargs={'pk': self.object.id})
        return context


class TypesDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesTypes
    form_class = MachinesTypesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:types_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف نوع ماكينة: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Machines:types_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        my_form = MachinesTypes.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 1
        my_form.save()
        return redirect(self.get_success_url())


class TypesRestore(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesTypes
    form_class = MachinesTypesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ارجاع نوع ماكينة: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Machines:types_restore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        my_form = MachinesTypes.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 0
        my_form.save()
        return redirect(self.get_success_url())


class TypesSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesTypes
    form_class = MachinesTypesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:types_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف نوع ماكينة بشكل نهائي: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Machines:types_super_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        my_form = MachinesTypes.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())