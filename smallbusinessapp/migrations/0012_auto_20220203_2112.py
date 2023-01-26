# Generated by Django 3.2.7 on 2022-02-04 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0011_businessdata_smallbusine_busines_b8d5d2_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='businessdata',
            name='smallbusine_busines_b8d5d2_idx',
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['state', 'naics_code'], name='smallbusine_state_23f032_idx'),
        ),
    ]