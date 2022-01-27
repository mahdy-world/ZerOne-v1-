from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from Machines.models import *
from SpareParts.models import *
# Create your models here.

invoice_choices = (
    (1, "فاتورة مبيعات"),
    (2, "فاتورة مرتجع مبيعات"),
    (3, "بيان أسعار"),
)

invoice_types = (
    (1, "مبيعات ماكينات"),
    (2, "مبيعات قطع غيار"),
)


class Invoice(models.Model):
    date = models.DateField(default=now, verbose_name='التاريخ')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='منشئ الفاتورة')
    invoice_product_type = models.IntegerField(choices=invoice_types, default=0, verbose_name='نوع المنتجات')
    invoice_type = models.IntegerField(choices=invoice_choices, default=0, verbose_name='نوع الفاتورة')
    customer = models.CharField(max_length=255, verbose_name='العميل')
    warehouse = models.ForeignKey(MachinesWarehouses, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='المخزن')
    warehouse_spare = models.ForeignKey(SparePartsWarehouses, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='المخزن')
    treasury = models.ForeignKey(WorkTreasury, on_delete=models.SET_NULL, null=True, verbose_name='الخزينة')
    total = models.FloatField(default=0.0, verbose_name='قيمة الفاتورة')
    discount = models.FloatField(default=0.0, verbose_name='الخصم')
    overall = models.FloatField(default=0.0, verbose_name='الإجمالي')
    comment = models.TextField(null=True, blank=True, verbose_name="ملاحظات")
    saved = models.BooleanField(default=False, verbose_name='حفظ')
    paid = models.BooleanField(default=False, verbose_name='دفع')
    paid_value = models.FloatField(default=0.0, verbose_name='القيمة المدفوعة')
    residual_value = models.FloatField(default=0.0, verbose_name='القيمة المتبقية')
    residual_value_pay_date = models.DateField(verbose_name='تاريخ اكمال الدفع', null=True)
    out_of_warehouse = models.BooleanField(default=False, verbose_name='خروج من المخزن')
    deleted = models.BooleanField(default=False, verbose_name='حذف')
    return_inv_id = models.IntegerField(default=0, verbose_name='رقم الفاتورة الأصلية')
    pay_type = models.CharField(max_length=255, verbose_name='نوع الدفع')

    def __str__(self):
        return str(self.id)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='الفاتورة')
    item = models.ForeignKey(MachinesNames, on_delete=models.SET_NULL, null=True, verbose_name='الصنف')
    item_spare = models.ForeignKey(SparePartsNames, on_delete=models.SET_NULL, null=True, verbose_name='الصنف')
    unit_price = models.FloatField(default=0.0, verbose_name='سعر البيع')
    quantity = models.FloatField(default=1.0, verbose_name='الكمية')
    total_price = models.FloatField(default=0.0, verbose_name='إجمالي')
    deleted = models.BooleanField(default=False, verbose_name='حذف المنتج من الفاتورة')

    def __str__(self):
        return str(self.invoice.id)


class InvoiceItemDetails(models.Model):
    invoice_item = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE, verbose_name='عنصر الفاتورة')
    quantity = models.FloatField(default=1.0, verbose_name='الكمية')
    undo = models.FloatField(default=0, verbose_name='الكمية المرتجعة')
    balance = models.FloatField(default=1.0, verbose_name='الرصيد')
    purchase_price = models.FloatField(default=0.0, verbose_name='سعر البيع')

    def __str__(self):
        return str(self.invoice_item.invoice.id)