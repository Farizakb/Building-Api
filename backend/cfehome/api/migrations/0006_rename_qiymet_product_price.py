# Generated by Django 4.1.3 on 2023-01-09 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_price_product_qiymet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='qiymet',
            new_name='price',
        ),
    ]