from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    selling_price = models.IntegerField()
    buying_price = models.IntegerField()
    inventory = models.IntegerField()
    mrp = models.IntegerField()

    def __str__(self):
        return str(self.product_name)


class Transaction(models.Model):
    customer_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    product_list = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)


    def __str(self):
        return str(self.product_list)