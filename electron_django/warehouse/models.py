from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category=models.CharField(unique=True,max_length=50)

    def __str__(self):
        return self.category

class Item(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='categories')
    location=models.CharField(max_length=10)
    quantity=models.IntegerField(default=0)
    image = models.ImageField(default='default_item.jpg', upload_to='items_pics')

    def __str__(self):
        return self.name

class ItemBySerial(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items')
    serial_number=models.CharField(max_length=100)
    moved_last=models.DateTimeField(auto_now_add=True)
    moved_until=models.DateTimeField(auto_now_add=True)
    moved_by_who=models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.serial_number