# Generated by Django 3.1.1 on 2020-11-19 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_orderitem_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='OrderedDate',
            new_name='ordered_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='startDate',
            new_name='start_date',
        ),
    ]