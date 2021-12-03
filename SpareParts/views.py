from django.shortcuts import get_object_or_404, redirect ,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import *
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.

# Spare Parts Type Module 
class SparePartsTypeList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    paginate_by = 8
    template_name = 'SpareParts/sparepartstypes_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['page'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

class SparePartsTypeTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    paginate_by = 8
    template_name = 'SpareParts/sparepartstypes_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'trach'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

class SparePartsTypeCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    form_class = SparePartsTypeForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة نوع قطعة غيار '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsTypeCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "  تم إضافة نوع قطعة غيار بنجاح", extra_tags="success")
        return reverse('SpareParts:SpareTypeList',)

    
class SparePartsTypeUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    form_class = SparePartsTypeForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل نوع قطعة غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsTypeUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل نوع قطعة غيار بنجاح ", extra_tags="info")
        return reverse('SpareParts:SpareTypeList',)


class SparePartsTypeDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    form_class = DeleteTypeForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SpareTypeList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف نوع قطعة غيار: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsTypeDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف نوع قطعة غيار " + str(self.object) + ' بنجاح ' , extra_tags="danger")
        myform = SparePartsTypes.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())

class SparePartsTypeRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    form_class = DeleteTypeForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SpareTypeTrachList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع نوع قطعة غيار: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsTypeRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع نوع قطعة غيار " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = SparePartsTypes.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())

#-----------------------------------------------------------------------------------------------------------------------------------

# Spare Parts Names Module 
class SparePartsNameList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsNames
    paginate_by = 8
    template_name = 'SpareParts/sparepartstnames_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['page'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

class SparePartsNameTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsNames
    paginate_by = 8
    template_name = 'SpareParts/sparepartsnames_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Name'] = 'trach'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

class SparePartsNameCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsNames
    form_class = SparePartsNameForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة أسم قطعة غيار '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "  تم اضافة اسم قطعة غيار بنجاح", extra_tags="success")
        return reverse('SpareParts:SparePartsNameList',)

    
class SparePartsNameUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsNames
    form_class = SparePartsNameForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل أسم قطعة غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل أسم قطعة غيار بنجاح ", extra_tags="info")
        return reverse('SpareParts:SparePartsNameList',)


class SparePartsNameDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsNames
    form_class = DeleteNameForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsNameList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف أسم قطعة غيار: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف أسم قطعة غيار " + str(self.object) + ' بنجاح ' , extra_tags="danger")
        myform = SparePartsNames.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())

class SparePartsNameRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsNames
    form_class = DeleteNameForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsNameList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع أسم قطعة غيار: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع نوع قطعة غيار " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = SparePartsNames.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())
