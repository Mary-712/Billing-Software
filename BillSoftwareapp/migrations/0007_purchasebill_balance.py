# Generated by Django 4.2.7 on 2024-01-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0006_alter_purchasebill_paidoff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasebill',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
