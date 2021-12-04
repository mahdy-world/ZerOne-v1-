from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib import messages


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
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة نوع ماكينة '
        context['message'] = 'create'
        context['action_url'] = reverse_lazy('Machines:types_create')
        return context

    def get_success_url(self):
        messages.success(self.request, "  تم إضافة نوع ماكينة بنجاح", extra_tags="success")
        return reverse('Machines:types_active_list')

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
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل نوع ماكينة: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Machines:types_update', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self):
        messages.success(self.request, " تم تعديل نوع ماكينة " + str(self.object) + " بنجاح ", extra_tags="success")
        return reverse('Machines:types_active_list')


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
        messages.success(self.request, " تم حذف نوع ماكينة " + str(self.object) + " بنجاح ", extra_tags="success")
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
        messages.success(self.request, " تم ارجاع نوع ماكينة " + str(self.object) + " بنجاح ", extra_tags="success")
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
        messages.success(self.request, " تم حذف نوع ماكينة " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = MachinesTypes.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


################################################################


class WarehousesActiveList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesWarehouses
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset


class WarehousesTrashList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesWarehouses
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'trash'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset


class WarehousesCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = MachinesWarehouses
    form_class = MachinesWarehousesForm
    template_name = 'forms/form_template.html'
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة مخزن ماكينات '
        context['message'] = 'create'
        context['action_url'] = reverse_lazy('Machines:warehouses_create')
        return context

    def get_success_url(self):
        messages.success(self.request, "  تم إضافة مخزن ماكينات بنجاح", extra_tags="success")
        return reverse('Machines:warehouses_active_list')

    # def get_success_url(self):
    #     if self.request.POST.get('url'):
    #         return self.request.POST.get('url')
    #     else:
    #         return self.success_url


class WarehousesUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesWarehouses
    form_class = MachinesWarehousesForm
    template_name = 'forms/form_template.html'
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل مخزن ماكينات: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Machines:warehouses_update', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self):
        messages.success(self.request, " تم تعديل مخزن ماكينات " + str(self.object) + " بنجاح ", extra_tags="success")
        return reverse('Machines:warehouses_active_list')


class WarehousesDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesWarehouses
    form_class = MachinesWarehousesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:warehouses_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف مخزن ماكينات: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Machines:warehouses_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مخزن ماكينات " + str(self.object) + " بنجاح ", extra_tags="success")
        my_form = MachinesWarehouses.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 1
        my_form.save()
        return redirect(self.get_success_url())


class WarehousesRestore(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesWarehouses
    form_class = MachinesWarehousesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:warehouses_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ارجاع مخزن ماكينات: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Machines:warehouses_restore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع مخزن ماكينات " + str(self.object) + " بنجاح ", extra_tags="success")
        my_form = MachinesWarehouses.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 0
        my_form.save()
        return redirect(self.get_success_url())


class WarehousesSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesWarehouses
    form_class = MachinesWarehousesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:warehouses_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف مخزن ماكينات بشكل نهائي: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Machines:warehouses_super_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مخزن ماكينات " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = MachinesWarehouses.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


################################################################


class NamesActiveList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesNames
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset


class NamesTrashList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesNames
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'trash'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset


class NamesCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = MachinesNames
    form_class = MachinesNamesForm
    template_name = 'forms/form_template.html'
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة صنف ماكينة '
        context['message'] = 'create'
        context['action_url'] = reverse_lazy('Machines:names_create')
        return context

    def get_success_url(self):
        messages.success(self.request, "  تم إضافة صنف ماكينة بنجاح", extra_tags="success")
        return reverse('Machines:names_active_list')

    # def get_success_url(self):
    #     if self.request.POST.get('url'):
    #         return self.request.POST.get('url')
    #     else:
    #         return self.success_url


class NamesUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesNames
    form_class = MachinesNamesForm
    template_name = 'forms/form_template.html'
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل صنف ماكينة: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Machines:names_update', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self):
        messages.success(self.request, " تم تعديل صنف ماكينة " + str(self.object) + " بنجاح ", extra_tags="success")
        return reverse('Machines:names_active_list')


class NamesDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesNames
    form_class = MachinesNamesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:names_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف صنف ماكينة: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Machines:names_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف صنف ماكينة " + str(self.object) + " بنجاح ", extra_tags="success")
        my_form = MachinesNames.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 1
        my_form.save()
        return redirect(self.get_success_url())


class NamesRestore(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesNames
    form_class = MachinesNamesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:names_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ارجاع صنف ماكينة: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Machines:names_restore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع صنف ماكينة " + str(self.object) + " بنجاح ", extra_tags="success")
        my_form = MachinesNames.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 0
        my_form.save()
        return redirect(self.get_success_url())


class NamesSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesNames
    form_class = MachinesNamesFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:names_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف صنف ماكينة بشكل نهائي: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Machines:names_super_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف صنف ماكينة " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = MachinesNames.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


################################################################


class SuppliersActiveList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesSuppliers
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('id')
        return queryset


class SuppliersTrashList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = MachinesSuppliers
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'trash'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('id')
        return queryset


class SuppliersCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = MachinesSuppliers
    form_class = MachinesSuppliersForm
    template_name = 'forms/form_template.html'
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة مورد ماكينات '
        context['message'] = 'create'
        context['action_url'] = reverse_lazy('Machines:suppliers_create')
        return context

    def get_success_url(self):
        messages.success(self.request, "  تم إضافة مورد ماكينات بنجاح", extra_tags="success")
        return reverse('Machines:suppliers_active_list')

    # def get_success_url(self):
    #     if self.request.POST.get('url'):
    #         return self.request.POST.get('url')
    #     else:
    #         return self.success_url


class SuppliersUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesSuppliers
    form_class = MachinesSuppliersForm
    template_name = 'forms/form_template.html'
    # success_url = reverse_lazy('Machines:types_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل مورد ماكينات: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Machines:suppliers_update', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self):
        messages.success(self.request, " تم تعديل مورد ماكينات " + str(self.object) + " بنجاح ", extra_tags="success")
        return reverse('Machines:suppliers_active_list')


class SuppliersDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesSuppliers
    form_class = MachinesSuppliersFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:suppliers_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف مورد ماكينات: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Machines:suppliers_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مورد ماكينات " + str(self.object) + " بنجاح ", extra_tags="success")
        my_form = MachinesSuppliers.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 1
        my_form.save()
        return redirect(self.get_success_url())


class SuppliersRestore(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesSuppliers
    form_class = MachinesSuppliersFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:suppliers_active_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ارجاع مورد ماكينات: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Machines:suppliers_restore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم ارجاع مورد ماكينات " + str(self.object) + " بنجاح ", extra_tags="success")
        my_form = MachinesSuppliers.objects.get(id=self.kwargs['pk'])
        my_form.deleted = 0
        my_form.save()
        return redirect(self.get_success_url())


class SuppliersSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = MachinesSuppliers
    form_class = MachinesSuppliersFormDelete
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Machines:suppliers_trash_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف مورد ماكينات بشكل نهائي: ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Machines:suppliers_super_delete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف مورد ماكينات " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = MachinesSuppliers.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())