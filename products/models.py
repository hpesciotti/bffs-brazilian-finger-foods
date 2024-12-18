from django.db import models

# Options for poduct model
COOKING_PROCESS_CHOICES = [
    (1, "Baked"),
    (2, "Fried"),
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

class Allergens(models.Model):
    """
    Similarly to dietary categories, this model maintains the allergens. 
    In the same manner, more than one allergen can be assigned to 
    a product (many-to-many relationship).
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Allergen"
        verbose_name_plural = "Allergens"

# Main Product model
class Product(models.Model):
    """
    Establishes the products to be sold by the website as part of its catalogue. 
    Products are unique, and quantities and expiry dates for stock functions 
    are handled by the model Batch. Includes the basic information offered 
    to customers, such as dietary information, allergens, cooking process 
    and other relevant details for filtering and display.
    """
    name = models.CharField(max_length=255, unique=True)
    dietary_categories = models.ManyToManyField(
        DietaryCategory, blank=True, related_name="products")
    dietary_info = models.TextField(blank=True, null=True)
    cooking_process = models.IntegerField(
        choices=COOKING_PROCESS_CHOICES, default=1)
    allergens = models.ManyToManyField(
        Allergens, blank=True, related_name="products")
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    image = models.ImageField(
        upload_to="products/images/", blank=True, null=True)

    def __str__(self):
        return self.name

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
        Product, on_delete=models.CASCADE, related_name="batches")
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
    
