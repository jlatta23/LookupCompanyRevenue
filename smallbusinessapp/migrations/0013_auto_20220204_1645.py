# Generated by Django 3.2.7 on 2022-02-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0012_auto_20220203_2112'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='businessdata',
            name='smallbusine_zip_cod_b9eb1f_idx',
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['zip_code'], name='smallbusine_zip_cod_efa2f7_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['zip_code', 'naics_code'], name='smallbusine_zip_cod_4bf834_idx'),
        ),
    ]