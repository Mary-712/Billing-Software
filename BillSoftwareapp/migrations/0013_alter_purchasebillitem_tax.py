# Generated by Django 4.2.7 on 2024-01-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0012_remove_itemmodel_tax_purchasebillitem_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebillitem',
            name='tax',
            field=models.CharField(max_length=100, null=True),
        ),
    ]