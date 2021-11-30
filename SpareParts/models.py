from django.db import models


# Create your models here.
class SparePartsUnits(models.Model):
    name = models.CharField(max_length=128, verbose_name='الاسم')
    deleted = models.BooleanField(default=False, verbose_name='مسح')

    def __str__(self):
        return self.name


class SparePartsTypes(models.Model):
    name = models.CharField(max_length=128, verbose_name='الاسم')
    deleted = models.BooleanField(default=False, verbose_name='مسح')

    def __str__(self):
        return self.name


class SparePartsWarehouses(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم المخزن')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SparePartsSuppliers(models.Model):
    name = models.CharField(max_length=250, verbose_name='اسم المورد')
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    initial_balance = models.FloatField(default=0, verbose_name='الرصيد الافتتاحي')
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name


class SparePartsOrders(models.Model):
    supplier = models.ForeignKey(SparePartsSuppliers, on_delete=models.CASCADE, null=True, verbose_name='المورد')
    name = models.CharField(max_length=250, verbose_name='اسم المورد')
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    initial_balance = models.FloatField(default=0, verbose_name='الرصيد الافتتاحي')
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name