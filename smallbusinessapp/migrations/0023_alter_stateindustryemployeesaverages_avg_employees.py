# Generated by Django 3.2.7 on 2022-02-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0022_auto_20220214_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateindustryemployeesaverages',
            name='avg_employees',
            field=models.FloatField(),
        ),
    ]