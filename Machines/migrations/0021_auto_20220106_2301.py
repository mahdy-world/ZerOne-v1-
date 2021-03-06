# Generated by Django 3.2.5 on 2022-01-06 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpareParts', '0017_auto_20211221_2202'),
        ('Machines', '0020_auto_20220106_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinenotifecation',
            name='spare_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartsorders', verbose_name='طلبية قطع الغيار'),
        ),
        migrations.AlterField(
            model_name='machinenotifecation',
            name='machine_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Machines.machinesorders', verbose_name='طلبية المكن'),
        ),
        migrations.AlterField(
            model_name='machinenotifecation',
            name='notifeaction_type',
            field=models.IntegerField(choices=[(1, 'موعد دفع عربون مكينة'), (2, 'موعد دفع باقي مبلغ مكينة'), (3, 'موعد استلام بضاعة مكينة'), (4, 'موعد دفع ضرائب مكينة')], default=0, verbose_name='نوع الاشعار'),
        ),
    ]
