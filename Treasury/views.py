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
        context['title'] = 'قائمة خزائن العمل'
        context['icons'] = '<i class="fas fa-coins"></i>'
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
        context['title'] = 'سلة مهملات خزائن العمل'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
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

#--------------------------------------------------------------------------------------------------------------------------------------------------#


class HomeTreasuryList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = HomeTreasury
    paginate_by = 8
    template_name = 'Treasury/hometreasury_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['title'] = 'قائمة خزائن البيت'
        context['icons'] = '<i class="fas fa-coins"></i>'
        context['page'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

class HomeTreasuryTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = HomeTreasury
    paginate_by = 8
    template_name = 'Treasury/hometreasury_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'trach'
        context['title'] = 'سلة مهملات خزائن البيت'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

class HomeTreasuryCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = HomeTreasury
    form_class = HomeTreasuryForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة خزينة البيت '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('Treasury:HomeTreasuryCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم اضافة خزينة البيت بنجاح", extra_tags="success")
        return reverse('Treasury:HomeTreasuryList',)

class HomeTreasuryUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = HomeTreasury
    form_class = HomeTreasuryForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل خزينة البيت: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Treasury:HomeTreasuryUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل خزينة البيت بنجاح ", extra_tags="info")
        return reverse('Treasury:HomeTreasuryList',)

class HomeTreasuryDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = HomeTreasury
    form_class = HomeTreasuryDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('Treasury:HomeTreasuryList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف البيت: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Treasury:HomeTreasuryDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف خزينة البيت " + str(self.object) + ' بنجاح ' , extra_tags="danger")
        myform = HomeTreasury.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())

class HomeTreasuryRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = HomeTreasury
    form_class = HomeTreasuryDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('Treasury:HomeTreasuryTrachList',)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع خزينة البيت: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Treasury:HomeTreasuryRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع خزينة البيت " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = HomeTreasury.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())
    

class HomeTreasurySuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = HomeTreasury
    form_class = HomeTreasuryDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Treasury:HomeTreasuryTrachList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف خزينة البيت: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Treasury:WorkTreasurySuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف خزينة البيت " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = WorkTreasury.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())    

#--------------------------------------------------------------------------------------------------------------------------------------------------#




class BankAccountList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = BankAccount
    paginate_by = 8
    template_name = 'Treasury/bankccount_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['title'] = 'قائمة حسابات البنك'
        context['icons'] = '<i class="fas fa-coins"></i>'
        context['page'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

class BankAccountTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = BankAccount
    paginate_by = 8
    template_name = 'Treasury/bankaccount_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'trach'
        context['title'] = 'سلة مهملات حسابات البنك'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

class BankAccountCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = BankAccount
    form_class = BankAccountForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة حساب بنك '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('Treasury:BankAccountCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم اضافة حساب البنك بنجاح", extra_tags="success")
        return reverse('Treasury:BankAccountList',)

class BankAccountUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = BankAccount
    form_class = BankAccountForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل حساب البنك : ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Treasury:BankAccountUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل حساب البنك بنجاح ", extra_tags="info")
        return reverse('Treasury:BankAccountList',)

class BankAccountDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = BankAccount
    form_class = BankAccountDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('Treasury:BankAccountList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف حساب البنك: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Treasury:BankAccountDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف  حساب البنك " + str(self.object) + ' بنجاح ' , extra_tags="danger")
        myform = BankAccount.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())

class BankAccountRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = BankAccount
    form_class = BankAccountDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('Treasury:BankAccountTrachList',)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع  حساب البنك: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Treasury:BankAccountRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع  حساب البنك " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = BankAccount.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())
    

class BankAccountSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = BankAccount
    form_class = BankAccountDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Treasury:BankAccountTrachList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف  حساب البنك: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Treasury:WorkTreasurySuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف حساب البنك " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = WorkTreasury.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())    

#--------------------------------------------------------------------------------------------------------------------------------------------------#