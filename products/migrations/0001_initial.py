# Generated by Django 5.1.4 on 2024-12-21 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietaryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Dietary Category',
                'verbose_name_plural': 'Dietary Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the name in lowercase, separated by underscores.', max_length=100, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('short_widget_name', models.CharField(max_length=255)),
                ('energy_kj', models.DecimalField(decimal_places=2, max_digits=7)),
                ('energy_kcal', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugars', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cooking_process', models.IntegerField(choices=[(1, 'Baked'), (2, 'Fried'), (3, 'Fried or Baked')], default=1)),
                ('allergens', models.CharField(help_text='Enter allergens separated by commas. Example: Dairy, Eggs, Nuts', max_length=255)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('best_seller', models.BooleanField(default=False)),
                ('image_large', models.ImageField(blank=True, null=True, upload_to='products/large/')),
                ('image_large_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image_widget', models.ImageField(blank=True, null=True, upload_to='products/widgets/')),
                ('image_widget_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('dietary_categories', models.ManyToManyField(related_name='products', to='products.dietarycategory')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
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
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batches',
                'ordering': ['expiry_date'],
            },
        ),
    ]
