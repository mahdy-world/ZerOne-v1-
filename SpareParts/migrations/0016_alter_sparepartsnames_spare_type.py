# Generated by Django 3.2.5 on 2021-12-19 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpareParts', '0015_sparepartsnames_spare_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepartsnames',
            name='spare_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartstypes', verbose_name='نوع قطعة الغيار'),
            preserve_default=False,
        ),
    ]
