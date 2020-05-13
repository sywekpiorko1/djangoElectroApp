from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Category(models.Model):
    category=models.CharField(unique=True,max_length=50)

    def __str__(self):
        return self.category

class Item(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='categories')
    location=models.CharField(max_length=10)
    quantity=models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(default='default_item.jpg', upload_to='items_pics')
    dailyRentCost=models.DecimalField(default=0, max_digits=6, decimal_places=2, validators=[MinValueValidator(0.00)])
    
    def __str__(self):
        return self.name  