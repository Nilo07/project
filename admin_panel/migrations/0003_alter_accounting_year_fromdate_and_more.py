# Generated by Django 4.1 on 2022-08-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_remove_accounting_year_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting_year',
            name='fromdate',
            field=models.CharField(default='April|1st', max_length=20),
        ),
        migrations.AlterField(
            model_name='accounting_year',
            name='todate',
            field=models.CharField(default='March|31st', max_length=20),
        ),
    ]