# Generated by Django 4.2.2 on 2023-07-26 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_order_amount_change_alter_order_grand_total_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bill',
        ),
    ]