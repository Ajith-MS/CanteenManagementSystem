from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50, null=True, blank=True)
    itemtype = models.CharField(max_length=50, null=True, blank=True)  # e.g., Veg, Non-Veg, etc.
    image = models.ImageField(upload_to='menu_images/')
    availablity = models.BooleanField(default=True)
    tags = models.JSONField(default=list)  # Store tags as a JSON field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    