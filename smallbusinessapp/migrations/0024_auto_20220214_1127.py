# Generated by Django 3.2.7 on 2022-02-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0023_alter_stateindustryemployeesaverages_avg_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCodeIndustryEmployeesAverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.TextField()),
                ('naics_code', models.TextField()),
                ('avg_employees', models.FloatField()),
            ],
        ),
        migrations.AddIndex(
            model_name='zipcodeindustryemployeesaverages',
            index=models.Index(fields=['naics_code', 'zip_code'], name='smallbusine_naics_c_351de5_idx'),
        ),
        migrations.AddIndex(
            model_name='zipcodeindustryemployeesaverages',
            index=models.Index(fields=['zip_code'], name='smallbusine_zip_cod_bfa58e_idx'),
        ),
        migrations.AddIndex(
            model_name='zipcodeindustryemployeesaverages',
            index=models.Index(fields=['naics_code'], name='smallbusine_naics_c_056e80_idx'),
        ),
    ]
