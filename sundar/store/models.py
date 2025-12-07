from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True)
    # stock = models.IntegerField(default=0)   # Add if needed
    # created_at = models.DateTimeField(auto_now_add=True)  # Add if needed
    def __str__(self):
        return self.name
