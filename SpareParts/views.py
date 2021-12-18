from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, redirect ,HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import *
from django.db.models import Count
from django.contrib import messages

from Treasury.models import WorkTreasuryTransactions

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
        context['title'] = 'قائمة انواع قطع الغيار'
        context['icons'] = '<i class="fas fa-shapes"></i>'
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
        context['title'] = 'سلة مهملات انواع قطع الغيار'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
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
    

class SparePartsTypeSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = SparePartsTypes
    form_class = DeleteTypeForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('SpareParts:SpareTypeTrachList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف نوع قطعة غيار بشكل نهائي: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsTypeSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف نوع قطعة غيار " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = SparePartsTypes.objects.get(id=self.kwargs['pk'])
        my_form.delete()
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
        context['title'] = 'قائمة أصناف قطع الغيار'
        context['icons'] = '<i class="fas fa-cubes"></i>'
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
        context['title'] = 'سلة مهملات أصناف قطع الغيار'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context


class SparePartsNameCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsNames
    form_class = SparePartsNameForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('SpareParts:SparePartsNameList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة صنف قطعة غيار '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "  تم اضافة صنف قطعة غيار بنجاح", extra_tags="success")
       
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url
   
class SparePartsNameUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsNames
    form_class = SparePartsNameForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل صنف قطعة غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل صنف قطعة غيار بنجاح ", extra_tags="info")
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
        context['title'] = 'نقل صنف قطعة غيار: ' + str(self.object) + 'الي سلة المهملات'
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم نقل صنف قطعة غيار " + str(self.object) + ' الي سلة المهملات بنجاح ' , extra_tags="danger")
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
        context['title'] = 'استرجاع صنف قطعة غيار: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع صنف قطعة غيار " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = SparePartsNames.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())

class SparePartsNameSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = SparePartsNames
    form_class = DeleteNameForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('SpareParts:SpareNameTrachList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف صنف قطعة غيار بشكل نهائي: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف صنف قطعة غيار " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = SparePartsNames.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())   



# Spare Parts Warehouse Module 
class SparePartsWarehouseList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    paginate_by = 8
    template_name = 'SpareParts/sparepartswarehouse_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['page'] = 'active'
        context['title'] = 'مخزن قطع الغيار'
        context['icons'] = '<i class="fas fa-warehouse"></i>'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

class SparePartsWarehouseTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    paginate_by = 8
    template_name = 'SpareParts/sparepartswarehouse_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Name'] = 'trach'
        context['title'] = 'سلة مهملات مخزن قطع الغيار'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

class SparePartsWarehouseCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    form_class = SparePartsWarehouseForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة مخزن قطع غيار '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsWarehouseCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "  تم اضافة مخزن قطع غيار بنجاح", extra_tags="success")
        return reverse('SpareParts:SparePartsWarehouseList',)

class SparePartsWarehouseUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    form_class = SparePartsWarehouseForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل مخزن قطع غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsWarehouseUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل مخزن قطع غيار بنجاح ", extra_tags="info")
        return reverse('SpareParts:SparePartsWarehouseList',)

class SparePartsWarehouseDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    form_class = WarehouseDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsWarehouseList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'نقل مخزن قطع غيار : ' + str(self.object) + 'الي سلة المهملات'
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsWarehouseDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم نقل مخزن قطع غيار " + str(self.object) + ' الي سلة المهملات بنجاح ' , extra_tags="danger")
        myform = SparePartsWarehouses.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())

class SparePartsWarehouseRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    form_class = WarehouseDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsWarehouseList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع مخزن قطع غيار: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsWarehouseRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع مخزن قطع غيار " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = SparePartsWarehouses.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())

class SparePartsWarehouseSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    form_class = WarehouseDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsWarehouseTrachList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف مخزن قطع الغيار بشكل نهائي: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsWarehouseSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مخزن قطع الغيار " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = SparePartsWarehouses.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url()) 
    


# Spare Parts Suppliers Module 
class SparePartsSupplierList(LoginRequiredMixin ,ListView):

    login_url = '/auth/login/'
    model = SparePartsSuppliers
    paginate_by = 8
    template_name = 'SpareParts/sparepartssuppliers_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['page'] = 'active'
        context['title'] = 'قائمة موردين قطع الغيار'
        context['icons'] = '<i class="fas fa-users"></i>'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context
    
class SparePartsSupplierTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsSuppliers
    paginate_by = 8
    template_name = 'SpareParts/sparepartssupplier_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Name'] = 'trach'
        context['title'] = 'سلة مهملات موردين قطع الغيار'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

class SparePartsSupplierCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsSuppliers
    form_class = SparePartSupplierForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة مورد قطع غيار '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsSupplierCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "  تم اضافة مورد قطع غيار بنجاح", extra_tags="success")
        return reverse('SpareParts:SparePartsSupplierList',)
    
class SparePartsSupplierUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsSuppliers
    form_class = SparePartSupplierForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل مورد قطع غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsSupplierUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم تعديل مورد قطع غيار بنجاح ", extra_tags="info")
        return reverse('SpareParts:SparePartsSupplierList',)

class SparePartsSupplierDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsSuppliers
    form_class = SupplierDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsSupplierList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'نقل مورد قطع غيار: ' + str(self.object) + 'الي سلة المهملات'
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsSupplierDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم نقل مورد قطع غيار " + str(self.object) + ' الي سلة المهملات بنجاح ' , extra_tags="danger")
        myform = SparePartsSuppliers.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())

class SparePartsSupplierRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsSuppliers
    form_class = SupplierDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsSupplierList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع مورد قطع غيار: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsSupplierRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع مورد قطع غيار " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = SparePartsSuppliers.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())

class SparePartsSupplierSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = SparePartsSuppliers
    form_class = SupplierDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsSupplierTrachList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف مورد قطع الغيار : ' + str(self.object) + 'بشكل نهائي'
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsSupplierSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مورد قطع الغيار " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = SparePartsSuppliers.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url()) 


# Spare Parts Orders Module 
class SparePartsOrderList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsOrders
    paginate_by = 8
    template_name = 'SpareParts/sparepartsorders_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['page'] = 'active'
        context['title'] = 'سلة مهملات موردين قطع الغيار'
        context['icons'] = '<i class="fas fa-file-invoice"></i>'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context


class SparePartsOrderTrachList(LoginRequiredMixin ,ListView):
    login_url = '/auth/login/'
    model = SparePartsOrders
    paginate_by = 8
    template_name = 'SpareParts/sparepartsorders_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Name'] = 'trach'
        context['title'] = 'سلة مهملات طلبيات قطع الغيار'
        context['icons'] = '<i class="fas fa-trash-alt"></i>'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context


class SparePartsOrderCreate(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsOrders
    form_class = SparePartOrderForm
    template_name = 'forms/order_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة طلبية قطع غيار '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderCreate')
        return context
    
    def get_success_url(self, **kwargs):
        messages.success(self.request, "  تم اضافة طلبية قطع غيار بنجاح", extra_tags="success")
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk':self.object.id})


class SparePartsOrderUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsOrders

    def get_form_class(self, **kwargs):
        op1 = SparePartsOrderOperations.objects.filter(order_number=self.object, operation_type=1)
        op2 = SparePartsOrderOperations.objects.filter(order_number=self.object, operation_type=2)
        if op2:
            form_class_name = SparePartOrderFormOp2
        elif op1:
            form_class_name = SparePartOrderFormOp1
        else:
            form_class_name = SparePartOrderForm
        return form_class_name

    # form_class = SparePartOrderForm
    template_name = 'forms/order_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل طلبية قطع غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderUpdate', kwargs={'pk': self.object.id})
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=self.form_class)
        op1 = SparePartsOrderOperations.objects.filter(order_number=self.object, operation_type=1)
        op2 = SparePartsOrderOperations.objects.filter(order_number=self.object, operation_type=2)
        if op1 or op2:
            form.fields['order_supplier'].queryset = SparePartsSuppliers.objects.filter(id=self.object.order_supplier.id)
        return form
    
    def get_success_url(self,**kwargs):
        messages.success(self.request, "تم تعديل طلبية' قطع غيار بنجاح ", extra_tags="info")
        return reverse('SpareParts:SparePartsOrderList')


class SparePartsOrderDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsOrders
    form_class = OrderDeleteForm
    template_name = 'forms/order_form.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsOrderList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف طلب قطع غيار: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف طلب قطع غيار " + str(self.object) + ' بنجاح ' , extra_tags="danger")
        myform = SparePartsOrders.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())


class SparePartsOrderRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsOrders
    form_class = OrderDeleteForm
    template_name = 'forms/order_form.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsOrderList',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع طلب قطع غيار: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع طلب قطع غيار " + str(self.object) + ' بنجاح ' , extra_tags="dark")
        myform = SparePartsOrders.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())    


class SparePartsOrderSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = SparePartsOrders
    form_class = OrderDeleteForm
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsOrderTrachList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف طلب قطع الغيار : ' + str(self.object.order_number) + 'بشكل نهائي'
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف طلب قطع الغيار " + str(self.object.order_number) + " نهائيا بنجاح ", extra_tags="success")
        my_form = SparePartsOrders.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url()) 


def SparePartsOrderDetail(request, pk):
    order = get_object_or_404(SparePartsOrders , id=pk)
    product = SparePartsOrderProducts.objects.all().filter(product_order=order,)
    
    count_product = SparePartsOrderProducts.objects.all().filter(product_order=order).count()

    queryset = SparePartsOrderProducts.objects.all().filter(product_order=order,)
    total = queryset.aggregate(total=Sum('product_price')).get('total')
    quantity = queryset.aggregate(quantity=Sum('product_quantity')).get('quantity')
    
    op1 = SparePartsOrderOperations.objects.filter(order_number=order, operation_type=1)
    op2 = SparePartsOrderOperations.objects.filter(order_number=order, operation_type=2)
    op3 = SparePartsOrderOperations.objects.filter(order_number=order, operation_type=3)
    op4 = SparePartsOrderOperations.objects.filter(order_number=order, operation_type=4)
    
    

    form = orderProductForm
    type_page = "list"
    page = "active"
    action_url = reverse_lazy('SpareParts:AddProductOrder',kwargs={'pk':order.id})
    
    context = {
        'order' : order,
        'type' : type_page,
        'page' : page,
        'form' : form,
        'action_url' : action_url,
        'product':product,
        'count_product':count_product,
        'total' :total,
        'op1':op1,
        'op2':op2,
        'op3':op3,
        'op4':op4,
        'qu':quantity
        
    }
    return render(request, 'SpareParts/sparepartsorders_detail.html', context)


def AddProductOrder(request, pk):
    order = get_object_or_404(SparePartsOrders , id=pk)
    product = SparePartsOrderProducts.objects.filter(product_order=order).order_by('id')
    count_product = SparePartsOrderProducts.objects.all().filter(product_order=order).count()
    print(count_product)
    
    form = orderProductForm(request.POST or None)
    type_page = "list"
    page = "active"
    action_url = reverse_lazy('SpareParts:AddProductOrder',kwargs={'pk':order.id})
    
    context = {
        'order' : order,
        'type' : type_page,
        'page' : page,
        'form' : orderProductForm,
        'action_url' : action_url,
        'product':product,
        'count_product' : count_product
    }    
   
    if form.is_valid():
        obj = form.save(commit=False)
        obj.product_order = order 
        obj.save()
        return redirect('SpareParts:SparePartsOrderDetail', pk=order.id)
    
    
    return render(request, 'SpareParts/sparepartsorders_detail.html', context)        


class SparePartsOrderAddProductUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsOrderProducts
    form_class = orderProductForm
    template_name = 'forms/form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل المنتج: ' 
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderAddProductUpdate', kwargs={'pk': self.object.id, 'id': self.object.product_order.id})
        return context
    
    def get_success_url(self,**kwargs):
        messages.success(self.request, "تم تعديل بنجاح ", extra_tags="info")

        # if self.request.POST.get('url'):
        #     return self.request.POST.get('url')
        # else:
        #     return self.success_url
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk': self.kwargs['id']})

class SparePartsOrderAddProductDelete(LoginRequiredMixin,UpdateView):
    login_url = '/auth/login/'
    model = SparePartsOrderProducts
    form_class = orderProductDeleteForm
    template_name = 'forms/form_template.html'
    
    def get_success_url(self):
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk':self.kwargs['id']})
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف المنتج: ' 
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderAddProductDelete', kwargs={'pk': self.object.id, 'id': self.object.product_order.id})
        return context
    

    def form_valid(self, form):
        messages.success(self.request, " تم حذف  المنتج " + str(self.object.product_name) + " نهائيا بنجاح ", extra_tags="success")
        my_form = SparePartsOrderProducts.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())
        

# عملية دفع العربون
class SparePartsOperationCreateDeposit(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsOrderOperations
    form_class = OperationForm
    template_name = 'forms/form_template.html'


    def get_success_url(self):
        messages.success(self.request, " تمت دفع العربون بنجاح " , extra_tags="success")
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk':self.kwargs['pk']})

    def get_absolute_url(self):
        messages.success(self.request, "لم يتم دفع العربون .. لايوجد مال كافي داخل الخزنة ", extra_tags="danger")
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk': self.kwargs['pk']})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' دفع عربون ' 
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOperationCreateDeposit', kwargs={'pk':self.kwargs['pk']})
        return context
    
    def get_form(self, *args, **kwargs):
        order_number = get_object_or_404(SparePartsOrders, id=self.kwargs['pk'])
        form = super(SparePartsOperationCreateDeposit, self).get_form(*args, **kwargs)
        form.fields['operation_value'].initial = order_number.order_deposit_value
        return form

    def form_valid(self, form):
        order_number = get_object_or_404(SparePartsOrders, id=self.kwargs['pk'])
        treasury_balance = form.cleaned_data.get("treasury_name").balance
        operation_value = form.cleaned_data.get("operation_value")
        
        # اضافة في جدول عملية دفع العربون
        if float(treasury_balance) >= float(operation_value):
            myform = SparePartsOrderOperations()
            myform.order_number = order_number
            myform.operation_type = 1
            myform.operation_value = form.cleaned_data.get("operation_value")
            myform.treasury_name = form.cleaned_data.get("treasury_name")
            myform.save()
        
            # خصم قيمة العربون من الخزنة 
            treasury = WorkTreasury.objects.get(id=int(form.cleaned_data.get("treasury_name").id))
            treasury.balance -= form.cleaned_data.get("operation_value")
            treasury.save(update_fields=['balance'])   
            
            # اضافة في جدول عمليات الخزنة 
            trans = WorkTreasuryTransactions()
            trans.transaction = 'دفع قيمة عربون طلبية رقم' + str(self.kwargs['pk'])
            trans.treasury = form.cleaned_data.get("treasury_name")
            trans.transaction_type = 1 
            trans.value = form.cleaned_data.get("operation_value")
            trans.save()
            return redirect(self.get_success_url())
        else:
            return redirect(self.get_absolute_url())
        
        
        
#عملية باقي المبلغ 
class SparePartsOperationCreateReset(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsOrderOperations
    form_class = OperationForm
    template_name = 'forms/form_template.html'


    def get_success_url(self):
        messages.success(self.request, " تمت دفع باقي المبلغ بنجاح " , extra_tags="success")
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk':self.kwargs['pk']})

    def get_absolute_url(self):
        messages.success(self.request, "لم يتم دفع باقي المبلغ .. لايوجد مال كافي داخل الخزنة ", extra_tags="danger")
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' دفع باقي المبلغ ' 
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOperationCreateReset', kwargs={'pk':self.kwargs['pk']})
        return context

    def get_form(self, *args, **kwargs):
        order_number = get_object_or_404(SparePartsOrders, id=self.kwargs['pk'])
        order_products_val = SparePartsOrderProducts.objects.filter(product_order__id=self.kwargs['pk']).aggregate(sum=Sum('product_price')).get('sum')
        form = super(SparePartsOperationCreateReset, self).get_form(*args, **kwargs)
        form.fields['operation_value'].initial = float(order_products_val) - float(order_number.order_deposit_value)
        return form

    def form_valid(self, form):
        order_number = get_object_or_404(SparePartsOrders, id=self.kwargs['pk'])
        treasury_balance = form.cleaned_data.get("treasury_name").balance
        operation_value = form.cleaned_data.get("operation_value")
        
        # اضافة في جدول عملية  الطلب
        if float(treasury_balance) >= float(operation_value):
            myform = SparePartsOrderOperations()
            myform.order_number = order_number
            myform.operation_type = 2
            myform.operation_value = form.cleaned_data.get("operation_value")
            myform.treasury_name = form.cleaned_data.get("treasury_name")
            myform.save()
        
            # خصم قيمة باقي المبلغ من الخزنة 
            treasury = WorkTreasury.objects.get(id=int(form.cleaned_data.get("treasury_name").id))
            treasury.balance -= form.cleaned_data.get("operation_value")
            treasury.save(update_fields=['balance'])   
            
            # اضافة في جدول عمليات الخزنة 
            trans = WorkTreasuryTransactions()
            trans.transaction = 'دفع باقي مبلغ طلبية رقم' + str(self.kwargs['pk'])
            trans.treasury = form.cleaned_data.get("treasury_name")
            trans.transaction_type = 1 
            trans.value = form.cleaned_data.get("operation_value")
            trans.save()
            return redirect(self.get_success_url())
        else:
            return redirect(self.get_absolute_url())
        

# عملية تخليص البضاعة         
class SparePartsOperationCreateClearance(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsOrderOperations
    form_class = OperationsForm3
    template_name = 'forms/form_template.html'


    def get_success_url(self):
        messages.success(self.request, " تمت دفع  مبلغ تخليص البضاعة بنجاح " , extra_tags="success")
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk':self.kwargs['pk']})

    def get_absolute_url(self):
        messages.success(self.request, "لم يتم دفع مبلغ تخليص البضاعة .. لايوجد مال كافي داخل الخزنة ", extra_tags="danger")
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' دفع باقي المبلغ ' 
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOperationCreateClearance', kwargs={'pk':self.kwargs['pk']})
        return context

    def get_form(self, *args, **kwargs):
        form = super(SparePartsOperationCreateClearance, self).get_form(*args, **kwargs)
        form.fields['operation_value'].initial = 1.0
        return form


    def form_valid(self, form):
        order_number = get_object_or_404(SparePartsOrders, id=self.kwargs['pk'])
        treasury_balance = form.cleaned_data.get("treasury_name").balance
        operation_value = form.cleaned_data.get("operation_value")
        
        # اضافة في جدول عملية  الطلب
        if float(treasury_balance) >= float(operation_value):
            myform = SparePartsOrderOperations()
            myform.order_number = order_number
            myform.operation_type = 3
            myform.operation_value = form.cleaned_data.get("operation_value")
            myform.treasury_name = form.cleaned_data.get("treasury_name")
            myform.save()
        
            # خصم قيمة باقي المبلغ من الخزنة 
            treasury = WorkTreasury.objects.get(id=int(form.cleaned_data.get("treasury_name").id))
            treasury.balance -= form.cleaned_data.get("operation_value")
            treasury.save(update_fields=['balance'])   
            
            # اضافة في جدول عمليات الخزنة 
            trans = WorkTreasuryTransactions()
            trans.transaction = 'دفع باقي مبلغ طلبية رقم' + str(self.kwargs['pk'])
            trans.treasury = form.cleaned_data.get("treasury_name")
            trans.transaction_type = 1 
            trans.value = form.cleaned_data.get("operation_value")
            trans.save()
            return redirect(self.get_success_url())
        else:
            return redirect(self.get_absolute_url())        
  
  
   
#عملية استلام  البضاعة 
class SparePartsOperationCreateOrder(LoginRequiredMixin ,CreateView):
    login_url = '/auth/login/'
    model = SparePartsOrderOperations
    form_class = OperationsForm2
    template_name = 'forms/form_template.html'
    

    def get_success_url(self):
        return reverse('SpareParts:SparePartsOrderDetail', kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استلام البضاعة' 
        context['message'] = 'operation'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOperationCreateOrder', kwargs={'pk':self.kwargs['pk']})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تمت العملية بنجاح " , extra_tags="success")
        order_number = get_object_or_404(SparePartsOrders , id=self.kwargs['pk'])
        myform = SparePartsOrderOperations()
        myform.order_number = order_number
        myform.operation_type=4
        myform.warehouse_name = form.cleaned_data.get("warehouse_name")
        myform.save()
        
        order_products = SparePartsOrderProducts.objects.filter(product_order=order_number, deleted=0)
        order_op3 = SparePartsOrderOperations.objects.get(order_number=order_number, operation_type=4)
        for product in order_products:
            price_cost = (float(product.product_price) / float(product.product_quantity)) + (float(order_op3.operation_value) / float(product.product_quantity))
            transactions_filter = SparePartsWarehouseTransactions.objects.filter(item=product.product_name, warehouse=form.cleaned_data.get("warehouse_name"), price_cost=price_cost)
            if transactions_filter:
                transaction = SparePartsWarehouseTransactions.objects.get(item=product.product_name, warehouse=form.cleaned_data.get("warehouse_name"), price_cost=price_cost)
                transaction.quantity += product.product_quantity
                transaction.save(update_fields=['quantity'])
            else:
                transaction = SparePartsWarehouseTransactions()
                transaction.warehouse = form.cleaned_data.get("warehouse_name")
                transaction.item = product.product_name
                transaction.quantity = product.product_quantity
                transaction.price_cost = price_cost
                transaction.save()

        return redirect(self.get_success_url())   
    

# عرض تفاصيل المخزن    

class SparePartsWarehouseDetail(LoginRequiredMixin, DetailView):
    login_url = '/auth/login/'
    model = SparePartsWarehouses
    template_name = 'SpareParts/sparepartswharehouse_detail.html'
    
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تفاصيل المخزن' 
        context['type'] = 'list'
        context['icons'] = '<i class="fas fa-warehouse"></i>'
        queryset = SparePartsWarehouseTransactions.objects.filter(warehouse=self.kwargs['pk'])
        context['count'] = queryset.count()
        context['all'] = queryset
        return context
    
