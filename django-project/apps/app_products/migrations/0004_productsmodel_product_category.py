# Generated by Django 5.2.3 on 2025-06-16 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_productsmodel_product_show_in_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='app_products.productscategory'),
        ),
    ]
