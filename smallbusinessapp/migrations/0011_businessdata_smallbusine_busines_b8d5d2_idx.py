# Generated by Django 3.2.7 on 2022-02-04 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0010_auto_20220202_1920'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['business_name', 'naics_code'], name='smallbusine_busines_b8d5d2_idx'),
        ),
    ]
