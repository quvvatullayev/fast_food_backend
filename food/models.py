from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='subcategories')
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products')
    price = models.IntegerField()
    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    hour = models.DateTimeField()
    def __str__(self):
        return self.name