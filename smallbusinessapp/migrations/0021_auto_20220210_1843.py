# Generated by Django 3.2.7 on 2022-02-11 00:43

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0020_businessdata_smallbusine_naics_c_6de661_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='businessdata',
            name='smallbusine_naics_c_6de661_idx',
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=django.contrib.postgres.indexes.HashIndex(fields=['naics_code'], name='smallbusine_naics_c_cdb9ef_hash'),
        ),
    ]
