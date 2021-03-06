# Generated by Django 3.2.5 on 2022-01-26 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpareParts', '0017_auto_20211221_2202'),
        ('Invoices', '0005_auto_20220124_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='warehouse_spare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SpareParts.sparepartswarehouses', verbose_name='المخزن'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='item_spare',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SpareParts.sparepartsnames', verbose_name='الصنف'),
        ),
    ]
