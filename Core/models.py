from django.db import models
from django.db.models.fields import CharField, DateTimeField

# Create your models here.

class SystemInformation(models.Model):
    name = models.CharField(null=True, max_length=50, verbose_name="اسم صاحب النظام")
    phone = models.IntegerField(null=True, verbose_name="رقم الموبيل")
    address = models.CharField(max_length=150, null=True, verbose_name="العنوان")
    
    def __str__(self):
        return self.name