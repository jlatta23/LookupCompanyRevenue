# Generated by Django 3.2.7 on 2022-06-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0024_auto_20220214_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='num_businesses',
            field=models.IntegerField(default=0),
        ),
    ]
