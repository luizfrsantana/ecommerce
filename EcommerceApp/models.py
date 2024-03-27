from django.db import models
# Create your models here.

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    stock = models.IntegerField()
    categoryID = models.ForeignKey(Category)

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderDate = models.DateTimeField()
    
class OrderDetails(models.Model):
    orderDetailID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    orderID = orderID = models.ForeignKey(Order)
    paymentDate = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_OPTIONS = (
        ('Credit', 'credit'),
        ('Debit', 'debit'),
        ('Cash', 'cash'),
    )
    paymentMethod = models.CharField(max_length=100, choices = PAYMENT_OPTIONS)
    
class Shipping(models.Model):
    shippingID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(Order)
    shipDate = models.DateTimeField()
    deliveryDate = models.DateTimeField()
    STATUS_OPTIONS = (
        ('Processing', 'processing'),
        ('Out for delivery', 'out for delivery'),
        ('Delivered', 'delivered'),
        ('Cancelled', 'cancelled')
    )
    status = models.CharField(max_length=100, choices = STATUS_OPTIONS)
    

    
    