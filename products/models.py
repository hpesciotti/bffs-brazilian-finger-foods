from django.db import models

# Options for poduct model
COOKING_PROCESS_CHOICES = [
    (1, "Baked"),
    (2, "Fried"),
    (3, "Fried or Baked"), # alteração
]

# Options for batch model
OFFER_CHOICES = [
    (1, "No Offer"),
    (2, "Discount"),
]

# Part of Product model dietary_categories field
class DietaryCategory(models.Model):
    """
    This model is responsible for maintaining the possible dietary categories.
    The model was created to add more than one unique dietary 
    category to a product. Initially, the dietary categories were an integer
    choice field, which would not make it possible to add more than one 
    dietary category to a product.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dietary Category"
        verbose_name_plural = "Dietary Categories"

# Main Model
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, unique=True,
        help_text="Enter the name in lowercase, separated by underscores.")
    full_name = models.CharField(max_length=255)
    short_widget_name = models.CharField(max_length=255)
    dietary_categories = models.ManyToManyField("DietaryCategory",
     related_name="products")
    energy_kj = models.DecimalField(max_digits=7, decimal_places=2)
    energy_kcal = models.DecimalField(max_digits=7, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
    sugars = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    salt = models.DecimalField(max_digits=5, decimal_places=2)
    fiber = models.DecimalField(max_digits=5, decimal_places=2)
    cooking_process = models.IntegerField(choices=COOKING_PROCESS_CHOICES,
     default=1)
    allergens = models.CharField(
        max_length=255,
        help_text="Enter allergens separated by commas. Example: Dairy, Eggs, Nuts",
    )
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    best_seller = models.BooleanField(default=False)
    image_large = models.ImageField(upload_to="products/large/",
     blank=True, null=True)
    image_widget = models.ImageField(upload_to="products/widgets/",
     blank=True, null=True)

    def __str__(self):
        return self.short_widget_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

# Batch model
class Batch(models.Model):
    """
    This model establishes the parameters for creating a batch of an
    existing product. The model aims to make it possible for the
    store owner to maintain an inventory of the shop stock.
    The model is comprised of unique batch numbers,
    expiry dates, stock quantities, and potential discounts.
    """
    product = models.ForeignKey(
        Product, to_field='product_id', on_delete=models.CASCADE,
         related_name="batches")
    batch_number = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    offer = models.IntegerField(
        choices=OFFER_CHOICES, default=0)
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.product.name} - Batch {self.batch_number}"

    class Meta:
        ordering = ["expiry_date"]
        verbose_name = "Batch"
        verbose_name_plural = "Batches"
