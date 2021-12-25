# Generated by Django 3.2.5 on 2021-12-23 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Machines', '0013_maintenance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinesorderproducts',
            name='product_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Machines.machinesnames', verbose_name='المنتج'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machines.machinesnames', verbose_name='المكينة'),
        ),
    ]