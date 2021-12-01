from django.db import models


# Create your models here.
# انواع الماكينات
class MachinesTypes(models.Model):
    name = models.CharField(max_length=128, verbose_name='الاسم')
    deleted = models.BooleanField(default=False, verbose_name='مسح')

    def __str__(self):
        return self.name


# مخازن الماكينات
class MachinesWarehouses(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم المخزن')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# اسماء الماكينات
class MachinesNames(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الصنف')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# موردين الماكينات
class MachinesSuppliers(models.Model):
    name = models.CharField(max_length=250, verbose_name='اسم المورد')
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    initial_balance = models.FloatField(default=0, verbose_name='الرصيد الافتتاحي')
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name


# فاتورة طلب الماكينات
class MachinesOrders(models.Model):
    order_number = models.CharField(max_length=50, null=True, verbose_name="رقم الطلب")
    order_date = models.DateTimeField(null=True, verbose_name="تاريخ الطلب")
    order_supplier = models.ForeignKey(MachinesSuppliers, on_delete=models.CASCADE, null=True, verbose_name='المورد')
    order_deposit_value = models.FloatField(default=0, null=True, verbose_name="قيمة العربون")
    order_deposit_date = models.DateTimeField(null=True, verbose_name="تاريخ دفع العربون")
    order_rest_date = models.DateTimeField(null=True, verbose_name="تاريخ دفع باقي المبلغ")
    order_receipt_date = models.DateTimeField(null=True, verbose_name="تاريخ استلام البضاعة")
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.order_number


# منتجات داخل فاتورة طلب الماكينات
class MachinesOrderProducts(models.Model):
    product_order = models.ForeignKey(MachinesOrders, on_delete=models.CASCADE, null=True, verbose_name='الطلبية')
    product_name = models.ForeignKey(MachinesNames, on_delete=models.CASCADE, null=True, verbose_name='المنج')
    product_quantity = models.IntegerField(default=0, null=True, verbose_name="الكمية")
    product_price = models.FloatField(default=0, null=True, verbose_name="سعر الشراء")
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.product_order