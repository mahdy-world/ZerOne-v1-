from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class WorkTreasury(models.Model):
    name = models.CharField(max_length=20, verbose_name="اسم الخزينة")
    initial_balance = models.FloatField(default=0, verbose_name='الرصيد الافتتاحي')
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
