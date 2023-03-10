# Generated by Django 3.2.7 on 2021-12-19 18:52

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations
from django.contrib.postgres.operations import BtreeGinExtension


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0003_auto_20211219_1235'),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.RemoveIndex(
            model_name='businessdata',
            name='smallbusine_busines_c15d8e_idx',
        ),
        migrations.AddField(
            model_name='businessdata',
            name='sv',
            field=django.contrib.postgres.search.SearchVectorField(default='Unknown name'),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='smallbusine_sv_62f516_gin'),
        ),
    ]
