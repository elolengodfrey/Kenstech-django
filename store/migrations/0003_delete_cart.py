# Generated by Django 4.1.7 on 2023-06-23 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_quantity_cartitem_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
