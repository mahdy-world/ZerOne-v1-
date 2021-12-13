from django.shortcuts import render

# Create your views here.
from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, redirect ,HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import *
from django.db.models import Count
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.

# Spare Parts Type Module 
class WorkTreasuryList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = WorkTreasury
    paginate_by = 8
    template_name = 'Treasury/worktreasury_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['page'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

class WorkTreasuryTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = WorkTreasury
    paginate_by = 8
    template_name = 'Treasury/worktreasury_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'trach'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

class WorkTreasuryCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = WorkTreasury
    form_class = WorkTreasuryForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة خزينة عمل '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('Treasury:WorkTreasuryCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم اضافة خزينة عمل بنجاح", extra_tags="success")
        return reverse('Treasury:WorkTreasuryList',)

class WorkTreasuryUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = WorkTreasury
    form_class = WorkTreasuryForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل خزينة عمل: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Treasury:WorkTreasuryUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل خزينة العمل بنجاح ", extra_tags="info")
        return reverse('Treasury:WorkTreasuryList',)

class WorkTreasuryDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = WorkTreasury
    form_class = WorkTreasuryDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('Treasury:WorkTreasuryList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف خزينةالعمل: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Treasury:WorkTreasuryDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف خزينة العمل " + str(self.object) + ' بنجاح ' , extra_tags="danger")
        myform = WorkTreasury.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())

class WorkTreasuryRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = WorkTreasury
    form_class = WorkTreasuryDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('Treasury:WorkTreasuryTrachList',)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع خزينة العمل: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Treasury:WorkTreasuryRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع خزينة العمل " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = WorkTreasury.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())
    

class WorkTreasurySuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = WorkTreasury
    form_class = WorkTreasuryDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Treasury:WorkTreasuryTrachList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف خزينة العمل: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Treasury:WorkTreasurySuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف خزينة العمل " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = WorkTreasury.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())    
