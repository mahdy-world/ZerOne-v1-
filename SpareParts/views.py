from django.shortcuts import get_object_or_404, redirect ,HttpResponseRedirect, render
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
        context['title'] = 'إضافة صنف قطعة غيار '
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "  تم اضافة صنف قطعة غيار بنجاح", extra_tags="success")
        return reverse('SpareParts:SparePartsNameList',)

    
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
        context['title'] = 'حذف صنف قطعة غيار: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsNameDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف صنف قطعة غيار " + str(self.object) + ' بنجاح ' , extra_tags="danger")
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
        context['title'] = 'حذف مخزن قطع غيار: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsWarehouseDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مخزن قطع غيار " + str(self.object) + ' بنجاح ' , extra_tags="danger")
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
        context['title'] = 'حذف مورد قطع غيار: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsSupplierDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مورد قطع غيار " + str(self.object) + ' بنجاح ' , extra_tags="danger")
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
        context['count'] = self.model.objects.filter(deleted=False).count()
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
    form_class = SparePartOrderForm
    template_name = 'forms/order_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل طلبية قطع غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('SpareParts:SparePartsOrderUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self,**kwargs):
        messages.success(self.request, "تم تعديل طلبية' قطع غيار بنجاح ", extra_tags="info")
        return reverse('SpareParts:SparePartsOrderDetail',kwargs={'pk': self.object.id})
    
    

def SparePartsOrderDetail(request, pk):
    order = get_object_or_404(SparePartsOrders , id=pk)
    product = SparePartsOrderProducts.objects.filter(product_order=order)
    print(product)
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
        'product':product
        
    }
    return render(request, 'SpareParts/sparepartsorders_detail.html', context)




def AddProductOrder(request, pk):
    order = get_object_or_404(SparePartsOrders , id=pk)
    product = SparePartsOrderProducts.objects.filter(product_order=order)
    
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
        'product':product
        
        
    }    
   
    if form.is_valid():
        obj = form.save(commit=False)
        obj.product_order = order 
        obj.save()
        return render(request, 'SpareParts/sparepartsorders_detail.html', context)        
    
    return render(request, 'SpareParts/sparepartsorders_detail.html', context)        
        