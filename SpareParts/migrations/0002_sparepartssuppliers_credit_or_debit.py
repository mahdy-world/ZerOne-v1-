# Generated by Django 3.2.5 on 2021-12-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpareParts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepartssuppliers',
            name='credit_or_debit',
            field=models.IntegerField(choices=[(2, 'عليك للمورد'), (1, 'لك عند المورد')], default=0, verbose_name='لك أم عليك'),
        ),
    ]