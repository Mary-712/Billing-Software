# Generated by Django 4.2.7 on 2024-01-22 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0017_remove_purchasebillitem_item_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parties',
            old_name='created_by',
            new_name='staff',
        ),
    ]
