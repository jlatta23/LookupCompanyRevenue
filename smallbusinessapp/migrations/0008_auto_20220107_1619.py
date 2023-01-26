# Generated by Django 3.2.7 on 2022-01-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbusinessapp', '0007_auto_20211221_1636'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='businessdata',
            name='smallbusine_zip_cod_efa2f7_idx',
        ),
        migrations.AddField(
            model_name='businessdata',
            name='zip_code_int',
            field=models.IntegerField(null=True),
        ),
        migrations.AddIndex(
            model_name='businessdata',
            index=models.Index(fields=['zip_code_int'], name='smallbusine_zip_cod_b9eb1f_idx'),
        ),
    ]
