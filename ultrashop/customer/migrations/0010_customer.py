# Generated by Django 4.2.5 on 2023-09-12 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0009_products_image2_products_image3'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('billing_address', models.CharField(max_length=255)),
                ('billing_address2', models.CharField(max_length=255, null=True)),
                ('credit_card_no', models.CharField(blank=True, max_length=255, null=True)),
                ('phoneno', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
