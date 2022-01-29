from django.db.models import Sum, Count, query
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import *
import weasyprint
from .models import *
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.http import HttpResponse
from Core.models import *

# Create your views here.


class InvoiceList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = Invoice
    paginate_by = 12

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False, invoice_product_type=self.kwargs['type']).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'active'
        context['invoice_product_type'] = self.kwargs['type']
        context['count'] = self.model.objects.filter(deleted=False, invoice_product_type=self.kwargs['type']).count()
        return context


class InvoiceTrashList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = Invoice
    paginate_by = 12

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True, invoice_product_type=self.kwargs['type']).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'trash'
        context['invoice_product_type'] = self.kwargs['type']
        context['count'] = self.model.objects.filter(deleted=True, invoice_product_type=self.kwargs['type']).count()
        return context


class InvoiceCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = Invoice
    # form_class = InvoiceForm
    def get_form_class(self, **kwargs):
        if self.kwargs['type'] == 1:
            form_class_name = InvoiceForm
        else:
            form_class_name = InvoiceSpareForm
        return form_class_name
    template_name = 'forms/form_template.html'
    # success_url = reverse_lazy('Invoices:InvoiceList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['type'] == 1:
            context['title'] = 'فاتورة مبيعات ماكينات'
        else:
            context['title'] = 'فاتورة مبيعات قطع غيار'
        context['message'] = 'create'
        context['action_url'] = reverse_lazy('Invoices:InvoiceCreate', kwargs={'type': self.kwargs['type']})
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=self.form_class)
        if self.kwargs['type'] == 1:
            form.fields['warehouse'].queryset = MachinesWarehouses.objects.filter(deleted=0)
        else:
            form.fields['warehouse_spare'].queryset = SparePartsWarehouses.objects.filter(deleted=0)
        return form

    def form_valid(self, form):
        form.save()
        obj = form.save(commit=False)
        myform = Invoice.objects.get(id=obj.id)
        myform.creator = self.request.user
        myform.invoice_type = 1
        myform.invoice_product_type = self.kwargs['type']
        myform.save()
        # return redirect(self.get_success_url())
        return redirect('Invoices:InvoiceDetail', pk=myform.id)

    def get_success_url(self, **kwargs):
        if self.kwargs['type'] == 1:
            messages.success(self.request, "تم اضافة مبيعات مكن بنجاح", extra_tags="success")
        else:
            messages.success(self.request, "تم اضافة مبيعات قطع غيار بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})


class InvoiceUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    # form_class = InvoiceForm
    def get_form_class(self, **kwargs):
        inv_item = InvoiceItem.objects.filter(invoice=self.object)
        if inv_item:
            form_class_name = InvoiceForm2
        else:
            if self.object.invoice_product_type == 1:
                form_class_name = InvoiceForm
            else:
                form_class_name = InvoiceSpareForm
        return form_class_name
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'تعديل فاتورة مبيعات مكن: ' + str(self.object)
        else:
            context['title'] = 'تعديل فاتورة مبيعات قطع غيار: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Invoices:InvoiceUpdate', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self, **kwargs):
        if self.object.invoice_product_type == 1:
            messages.success(self.request, "تم تعديل مبيعات مكن بنجاح", extra_tags="success")
        else:
            messages.success(self.request, "تم تعديل مبيعات قطع غيار بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceList', kwargs={'type': self.object.invoice_product_type})


class InvoiceSave(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceSaveForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'حفظ فاتورة مبيعات مكن: ' + str(self.object)
        else:
            context['title'] = 'حفظ فاتورة مبيعات قطع غيار: ' + str(self.object)
        context['message'] = 'inv_save'
        context['action_url'] = reverse_lazy('Invoices:InvoiceSave', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم حفظ الفاتورة بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.save()
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.saved = 1
        myform.save()
        return redirect(self.get_success_url())


class InvoiceBack(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceBackForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'الغاء حفظ فاتورة مبيعات مكن: ' + str(self.object)
        else:
            context['title'] = 'الغاء حفظ فاتورة مبيعات قطع غيار: ' + str(self.object)
        context['message'] = 'inv_back'
        context['action_url'] = reverse_lazy('Invoices:InvoiceBack', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        form.save()
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.saved = 0
        myform.discount = 0.0
        myform.overall = 0.0
        myform.save()
        return redirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم الغاء حفظ الفاتورة بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})


class InvoicePay(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoicePayForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'دفع فاتورة مبيعات مكن: ' + str(self.object)
        else:
            context['title'] = 'دفع فاتورة مبيعات قطع غيار: ' + str(self.object)
        context['message'] = 'inv_pay'
        context['paid'] = self.object.paid
        context['action_url'] = reverse_lazy('Invoices:InvoicePay', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        form.save()
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.paid = 1
        myform.save()

        object_paid_value = Invoice.objects.get(id=self.kwargs['pk']).paid_value
        paid_val = form.cleaned_data.get("paid_value")
        if self.object.paid == False:
            paid_value = paid_val
        else:
            paid_value = paid_val - object_paid_value

        treasury = self.object.treasury
        treasury.balance += paid_value
        treasury.save(update_fields=['balance'])

        trans = WorkTreasuryTransactions()
        trans.transaction = 'استلام قيمة مبيعات فاتورة مبيعات رقم ' + str(self.kwargs['pk'])
        trans.treasury = self.object.treasury
        trans.transaction_type = 2
        trans.value = paid_value
        trans.save()

        return redirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم دفع الفاتورة بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})


class InvoiceOut(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceOutForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'تسليم بضاعة فاتورة مبيعات مكن: ' + str(self.object)
        else:
            context['title'] = 'تسليم بضاعة فاتورة مبيعات قطع غيار: ' + str(self.object)
        context['message'] = 'out_ware'
        context['action_url'] = reverse_lazy('Invoices:InvoiceOut', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        form.save()
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.out_of_warehouse = 1
        myform.save()

        invoice = Invoice.objects.get(id=self.kwargs['pk'])
        invoice_items = InvoiceItem.objects.filter(invoice=invoice, deleted=0)
        for i in invoice_items:
            item_main_quant = float(i.quantity)
            while item_main_quant > 0:
                if invoice.invoice_product_type == 1:
                    transaction = WarehouseTransactions.objects.filter(item=i.item, warehouse=invoice.warehouse, quantity__gt=0).first()
                else:
                    transaction = SparePartsWarehouseTransactions.objects.filter(item=i.item_spare, warehouse=invoice.warehouse_spare, quantity__gt=0).first()
                if transaction:
                    transaction_quant = float(transaction.quantity)
                    item_main_quant_datail = 0
                    if transaction_quant < item_main_quant:
                        item_main_quant_datail = transaction_quant
                        transaction.quantity = 0.0
                        transaction.save(update_fields=['quantity'])
                        item_main_quant = item_main_quant - transaction_quant
                    elif transaction_quant > item_main_quant:
                        item_main_quant_datail = item_main_quant
                        transaction.quantity = transaction_quant - item_main_quant
                        transaction.save(update_fields=['quantity'])
                        item_main_quant = 0
                    elif transaction_quant == item_main_quant:
                        item_main_quant_datail = transaction_quant
                        transaction.quantity = 0.0
                        transaction.save(update_fields=['quantity'])
                        item_main_quant = 0

                    inv_item_detail = InvoiceItemDetails()
                    inv_item_detail.invoice_item = i
                    inv_item_detail.quantity = item_main_quant_datail
                    inv_item_detail.balance = item_main_quant_datail
                    if invoice.invoice_product_type == 1:
                        inv_item_detail.purchase_price = transaction.purchase_cost
                    else:
                        inv_item_detail.purchase_price = transaction.price_cost
                    inv_item_detail.save()

        return redirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم تسليم بضاعة الفاتورة بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})


class InvoiceDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceList', kwargs={'type': self.object.invoice_product_type})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'حذف فاتورة مبيعات مكن: ' + str(self.object)
        else:
            context['title'] = 'حذف فاتورة مبيعات قطع غيار: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Invoices:InvoiceDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        if self.object.invoice_product_type == 1:
            messages.success(self.request, " تم حذف مبيعات مكن " + str(self.object) + ' بنجاح ', extra_tags="danger")
        else:
            messages.success(self.request, " تم حذف مبيعات قطع غيار " + str(self.object) + ' بنجاح ', extra_tags="danger")
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())


class InvoiceRestore(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceTrashList', kwargs={'type': self.object.invoice_product_type})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'استرجاع فاتورة مبيعات مكن: ' + str(self.object)
        else:
            context['title'] = 'استرجاع فاتورة مبيعات قطع غيار: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Invoices:InvoiceRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        if self.object.invoice_product_type == 1:
            messages.success(self.request, " تم استرجاع مبيعات مكن " + str(self.object) + ' بنجاح ', extra_tags="dark")
        else:
            messages.success(self.request, " تم استرجاع مبيعات قطع غيار " + str(self.object) + ' بنجاح ', extra_tags="dark")
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())


class InvoiceSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceTrashList', kwargs={'type': self.object.invoice_product_type})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice_product_type == 1:
            context['title'] = 'حذف فاتورة مبيعات مكن : ' + str(self.object.id) + 'بشكل نهائي'
        else:
            context['title'] = 'حذف فاتورة مبيعات قطع غيار : ' + str(self.object.id) + 'بشكل نهائي'
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Invoices:InvoiceSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        if self.object.invoice_product_type == 1:
            messages.success(self.request, " تم حذف مبيعات مكن " + str(self.object.id) + " نهائيا بنجاح ", extra_tags="success")
        else:
            messages.success(self.request, " تم حذف مبيعات قطع غيار " + str(self.object.id) + " نهائيا بنجاح ", extra_tags="success")
        my_form = Invoice.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


def InvoiceDetail(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    product = InvoiceItem.objects.filter(invoice=invoice).order_by('id')
    count_product = product.count()

    total = product.aggregate(total=Sum('total_price')).get('total')
    quantity = product.aggregate(quantity=Sum('quantity')).get('quantity')

    if total:
        invoice.total = total
        invoice.save()

    if invoice.invoice_product_type == 1:
        form = MachinesInvoiceProductsForm()
    else:
        form = MachinesInvoiceSpareProductsForm()

    products = []
    for prod in product:
        if invoice.invoice_product_type == 1:
            products.append(prod.item.id)
        else:
            products.append(prod.item_spare.id)

    if invoice.warehouse:
        trans = WarehouseTransactions.objects.filter(quantity__gt=0, warehouse=invoice.warehouse).values_list('item', flat=True).distinct()
        form.fields['item'].queryset = MachinesNames.objects.filter(id__in=trans).exclude(id__in=products)
    else:
        trans = SparePartsWarehouseTransactions.objects.filter(quantity__gt=0, warehouse=invoice.warehouse_spare).values_list('item', flat=True).distinct()
        form.fields['item_spare'].queryset = SparePartsNames.objects.filter(id__in=trans).exclude(id__in=products)

    type_page = "list"
    page = "active"
    action_url = reverse_lazy('Invoices:AddProductInvoice', kwargs={'pk': invoice.id})

    context = {
        'invoice': invoice,
        'type': type_page,
        'page': page,
        'form': form,
        'action_url': action_url,
        'product': product,
        'count_product': count_product,
        'total': total,
        'qu': quantity,
        'date': datetime.now().date(),

    }
    return render(request, 'Invoices/invoice_detail.html', context)


def AddProductInvoice(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    product = InvoiceItem.objects.filter(invoice=invoice).order_by('id')
    count_product = product.count()

    if invoice.invoice_product_type == 1:
        form = MachinesInvoiceProductsForm(request.POST or None)
        formm = MachinesInvoiceProductsForm()
    else:
        form = MachinesInvoiceSpareProductsForm(request.POST or None)
        formm = MachinesInvoiceSpareProductsForm()
    type_page = "list"
    page = "active"
    action_url = reverse_lazy('Invoices:AddProductInvoice', kwargs={'pk': invoice.id})

    context = {
        'invoice': invoice,
        'type': type_page,
        'page': page,
        'form': formm,
        'action_url': action_url,
        'product': product,
        'count_product': count_product
    }

    if form.is_valid():
        quantity = form.cleaned_data.get("quantity")
        if invoice.invoice_product_type == 1:
            item = form.cleaned_data.get("item")
            trans = WarehouseTransactions.objects.filter(warehouse=invoice.warehouse, item=item).aggregate(quant=Sum('quantity')).get('quant')
        else:
            item_spare = form.cleaned_data.get("item_spare")
            trans = SparePartsWarehouseTransactions.objects.filter(warehouse=invoice.warehouse_spare, item=item_spare).aggregate(quant=Sum('quantity')).get('quant')
        if trans >= quantity:
            obj = form.save(commit=False)
            obj.invoice = invoice
            obj.save()
            messages.success(request, " تم اضافة منتج الي الفاتورة بنجاح ", extra_tags="success")
        else:
            messages.success(request, " لاتوجد كمية كافية من الصنف داخل المخزن ", extra_tags="danger")
        return redirect('Invoices:InvoiceDetail', pk=invoice.id)

    return render(request, 'Invoices/invoice_detail.html', context)


class InvoiceProductsUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = InvoiceItem
    # form_class = MachinesInvoiceProductsFormUpdate
    def get_form_class(self, **kwargs):
        if self.object.invoice.invoice_product_type == 1:
            form_class_name = MachinesInvoiceProductsFormUpdate
        else:
            form_class_name = MachinesInvoiceSpareProductsFormUpdate
        return form_class_name
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice.invoice_product_type == 1:
            context['title'] = 'تعديل المنتج: ' + str(self.object.item)
        else:
            context['title'] = 'تعديل المنتج: ' + str(self.object.item_spare)
        context['message'] = 'update'
        context['inv_update'] = 'update'
        context['action_url'] = reverse_lazy('Invoices:InvoiceProductsUpdate', kwargs={'pk': self.object.id, 'id': self.object.invoice.id})
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=self.form_class)
        if self.object.invoice.invoice_product_type == 1:
            form.fields['item'].queryset = MachinesNames.objects.filter(id=self.object.item.id)
        else:
            form.fields['item_spare'].queryset = SparePartsNames.objects.filter(id=self.object.item_spare.id)
        return form

    def get_success_url(self, **kwargs):
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.kwargs['id']})

    def form_valid(self, form):
        quantity = form.cleaned_data.get("quantity")
        if self.object.invoice.invoice_product_type == 1:
            item = form.cleaned_data.get("item")
            trans = WarehouseTransactions.objects.filter(warehouse=self.object.invoice.warehouse, item=item).aggregate(quant=Sum('quantity')).get('quant')
            object_item = self.object.item
        else:
            item_spare = form.cleaned_data.get("item_spare")
            trans = SparePartsWarehouseTransactions.objects.filter(warehouse=self.object.invoice.warehouse_spare, item=item_spare).aggregate(quant=Sum('quantity')).get('quant')
            object_item = self.object.item_spare

        if trans >= quantity:
            form.save()
            messages.success(self.request, " تم تعديل منتج " + str(object_item) + " بنجاح ", extra_tags="success")
        else:
            messages.success(self.request, " لاتوجد كمية كافية من الصنف داخل المخزن ", extra_tags="danger")
        return redirect(self.get_success_url())


class InvoiceProductsDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = InvoiceItem
    form_class = MachinesInvoiceProductsDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.kwargs['id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.invoice.invoice_product_type == 1:
            context['title'] = 'حذف المنتج: ' + str(self.object.item)
        else:
            context['title'] = 'حذف المنتج: ' + str(self.object.item_spare)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Invoices:InvoiceProductsDelete', kwargs={'pk': self.object.id, 'id': self.object.invoice.id})
        return context

    def form_valid(self, form):
        if self.object.invoice.invoice_product_type == 1:
            object_item = self.object.item
        else:
            object_item = self.object.item_spare
        messages.success(self.request, " تم حذف المنتج " + str(object_item) + " من الفاتورة بنجاح ", extra_tags="success")
        my_form = InvoiceItem.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


def PrintInvoice(request, id):
    date = datetime.now()
    invoice = Invoice.objects.get(id=id)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice, deleted=0)
    shop_setting = SystemInformation.objects.all()
    if shop_setting.count() > 0:
        shop_setting = shop_setting.last()
    else:
        shop_setting = None
    context = {
        'date': date,
        'user': request.user.username,
        'invoice': invoice,
        'invoice_items': invoice_items,
        'shop_setting': shop_setting,
    }
    html_string = render_to_string('Invoices/print_invoice.html', context)
    html = weasyprint.HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf(stylesheets=[weasyprint.CSS('static/assets/css/invoice_pdf.css')], presentational_hints=True)
    response = HttpResponse(pdf, content_type='application/pdf')
    return response
