# Generated by Django 3.2.7 on 2021-12-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.TextField()),
                ('address', models.TextField()),
                ('city', models.TextField(null=True)),
                ('state', models.TextField(null=True)),
                ('zip_code', models.TextField(null=True)),
                ('naics_code', models.TextField(null=True)),
                ('naics_name', models.TextField(null=True)),
                ('revenue_estimate', models.FloatField()),
                ('business_type', models.TextField(null=True)),
                ('loan_amount', models.FloatField(default=0)),
                ('owner_race', models.TextField(null=True)),
                ('owner_ethnicity', models.TextField(null=True)),
                ('num_employees', models.IntegerField(default=0)),
                ('payroll_proceed', models.FloatField(null=True)),
                ('payroll_annual', models.FloatField(null=True)),
                ('utilities_proceed', models.FloatField(default=0)),
                ('mortgage_proceed', models.FloatField(default=0)),
                ('rent_proceed', models.FloatField(default=0)),
                ('health_care_proceed', models.FloatField(default=0)),
                ('debt_interest_proceed', models.FloatField(default=0)),
                ('servicing_lender_name', models.TextField(null=True)),
                ('origination_lender_name', models.TextField(null=True)),
                ('business_age', models.TextField(null=True)),
                ('revenue_confidence', models.TextField(default='high')),
                ('approximate_naics_code', models.TextField()),
                ('revenue_to_payroll', models.FloatField()),
                ('revenue_range', models.TextField(null=True)),
                ('employee_range', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('abbreviation', models.TextField()),
                ('change', models.TextField()),
            ],
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['business_name', 'naics_name'], name='smallbusine_busines_d39f38_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['business_name', 'naics_name', 'revenue_estimate', 'num_employees', 'naics_name', 'address', 'state', 'zip_code'], name='smallbusine_busines_c2367f_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['business_name'], name='smallbusine_busines_c15d8e_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['revenue_estimate'], name='smallbusine_revenue_d32357_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['num_employees'], name='smallbusine_num_emp_07cbe9_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['naics_name'], name='smallbusine_naics_n_35df67_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['address'], name='smallbusine_address_daa574_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['state'], name='smallbusine_state_75f77e_idx'),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['zip_code'], name='smallbusine_zip_cod_efa2f7_idx'),
        ),
    ]