# Generated by Django 3.2.5 on 2021-12-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systeminformation',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='رقم الموبيل'),
        ),
    ]