from django.db import models


# Create your models here.

# انواع قطع الغيار
class SparePartsTypes(models.Model):
    name = models.CharField(max_length=128, verbose_name='الاسم')
    deleted = models.BooleanField(default=False, verbose_name='مسح')

    def __str__(self):
        return self.name


# مخازن قطع الغيار
class SparePartsWarehouses(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم المخزن')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# اسماء قطع الغيار
class SparePartsNames(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الصنف')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# موردين قطع الغيار
STATUS_CHOICES = (
    (2, "عليك للمورد"),
    (1, "لك عند المورد"),
    )

class SparePartsSuppliers(models.Model):
    name = models.CharField(max_length=250, verbose_name='اسم المورد')
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    initial_balance = models.FloatField(default=0, verbose_name='الرصيد الافتتاحي')
    credit_or_debit = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='لك أم عليك')
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name


# فاتورة الطلب
class SparePartsOrders(models.Model):
    order_number = models.CharField(max_length=50, null=True, verbose_name="رقم الطلب")
    order_date = models.DateTimeField(null=True, verbose_name="تاريخ الطلب")
    order_supplier = models.ForeignKey(SparePartsSuppliers, on_delete=models.CASCADE, null=True, verbose_name='المورد')
    order_deposit_value = models.FloatField(default=0, null=True, verbose_name="قيمة العربون")
    order_deposit_date = models.DateTimeField(null=True, verbose_name="تاريخ دفع العربون")
    order_rest_date = models.DateTimeField(null=True, verbose_name="تاريخ دفع باقي المبلغ")
    order_receipt_date = models.DateTimeField(null=True, verbose_name="تاريخ استلام البضاعة")
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.order_number


# منتجات داخل الفاتورة
class SparePartsOrderProducts(models.Model):
    product_order = models.ForeignKey(SparePartsOrders, on_delete=models.CASCADE, null=True, verbose_name='الطلبية')
    product_name = models.ForeignKey(SparePartsNames, on_delete=models.CASCADE, null=True, verbose_name='المنج')
    product_quantity = models.IntegerField(default=0, null=True, verbose_name="الكمية")
    product_price = models.FloatField(default=0, null=True, verbose_name="سعر الشراء")
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.product_order
