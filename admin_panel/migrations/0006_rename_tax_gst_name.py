# Generated by Django 3.2.14 on 2022-07-22 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_gst'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gst',
            old_name='tax',
            new_name='name',
        ),
    ]