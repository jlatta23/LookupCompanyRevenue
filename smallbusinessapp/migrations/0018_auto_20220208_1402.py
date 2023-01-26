# Generated by Django 3.2.7 on 2022-02-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0017_auto_20220208_1357'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='zipcodeindustryrevenueaverages',
            index=models.Index(fields=['naics_code', 'zip_code'], name='smallbusine_naics_c_e38d57_idx'),
        ),
        migrations.AddIndex(
            model_name='zipcodeindustryrevenueaverages',
            index=models.Index(fields=['zip_code'], name='smallbusine_zip_cod_ed29a0_idx'),
        ),
        migrations.AddIndex(
            model_name='zipcodeindustryrevenueaverages',
            index=models.Index(fields=['naics_code'], name='smallbusine_naics_c_b7bf11_idx'),
        ),
    ]