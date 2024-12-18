# Generated by Django 5.1.4 on 2024-12-18 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DietaryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('dietary_info', models.TextField(blank=True, null=True)),
                ('cooking_process', models.IntegerField(choices=[(1, 'Baked'), (2, 'Fried')], default=1)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('allergens', models.ManyToManyField(blank=True, related_name='products', to='products.allergens')),
                ('dietary_categories', models.ManyToManyField(blank=True, related_name='products', to='products.dietarycategory')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=100, unique=True)),
                ('expiry_date', models.DateTimeField()),
                ('quantity', models.PositiveIntegerField()),
                ('offer', models.IntegerField(choices=[(1, 'No Offer'), (2, 'Discount')], default=0)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batches', to='products.product')),
            ],
            options={
                'ordering': ['expiry_date'],
            },
        ),
    ]
