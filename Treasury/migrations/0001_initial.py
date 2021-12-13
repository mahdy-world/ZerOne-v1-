# Generated by Django 3.2.5 on 2021-12-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkTreasury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='اسم الخزينة')),
                ('initial_balance', models.FloatField(default=0, verbose_name='الرصيد الافتتاحي')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]