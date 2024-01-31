# Generated by Django 3.2.23 on 2024-01-19 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(max_length=255)),
                ('done_by_name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BillSoftwareapp.company')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BillSoftwareapp.itemmodel')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BillSoftwareapp.staff_details')),
            ],
        ),
    ]