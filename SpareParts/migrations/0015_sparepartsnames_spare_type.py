# Generated by Django 3.2.5 on 2021-12-19 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpareParts', '0014_auto_20211219_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepartsnames',
            name='spare_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartstypes', verbose_name='نوع قطعة الغيار'),
        ),
    ]