# Generated by Django 4.2.5 on 2023-09-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_products_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='availablility',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=45, null=True),
        ),
    ]
