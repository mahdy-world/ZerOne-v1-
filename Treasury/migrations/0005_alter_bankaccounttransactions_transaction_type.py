# Generated by Django 3.2.5 on 2021-12-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treasury', '0004_bankaccounttransactions_hometreasurytransactions_worktreasurytransactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccounttransactions',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'داخل للحساب'), (2, 'خارج من الحساب')], default=0, verbose_name='نوع العملية'),
        ),
    ]
