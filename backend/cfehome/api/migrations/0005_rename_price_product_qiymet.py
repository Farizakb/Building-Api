# Generated by Django 4.1.3 on 2023-01-09 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='qiymet',
        ),
    ]
