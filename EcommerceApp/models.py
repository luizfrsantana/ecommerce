from django.db import models
# Create your models here.

class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    
    def serialize(self):
        return{
            "id":self.customerID,
            "name":self.name,
            "email":self.email,
            "address":self.address,
            "phone":self.phone
        }
        
    def __str__(self):
        return f"Name: {self.name} - Email: {self.email}"

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def serialize(self):
        return {
            "categoryID": self.categoryID,
            "name": self.name,
            "description": self.description
        }
   
    def __str__(self):
        return f"Name: {self.name}"   
   
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    stock = models.IntegerField()
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def serialize(self):
        return {
            "productID": self.productID,
            "name": self.name,
            "price": str(self.price),
            "description": self.description,
            "stock": self.stock,
            "category": self.categoryID.serialize()
        }

    def __str__(self):
        return f"Produto: {self.name} - Price: {self.price}"

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderDate = models.DateTimeField()
    
    def serialize(self):
        return {
            "orderID": self.orderID,
            "customer": self.customerID.serialize(),
            "orderDate": self.OrderDate.strftime("%Y-%m-%d %H:%M:%S"),
        }
    
    def __str__(self):
        return f"Order ID: {self.orderID}"
    
class OrderDetails(models.Model):
    orderDetailID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def serialize(self):
        return {
            "orderDetailID": self.orderDetailID,
            "order": self.orderID.serialize(),
            "product": self.productID.serialize(),
            "quantity": self.quantity
        }
    
    def __str__(self):
        return f"OrderDetail ID: {self.orderDetailID}"
    
class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    orderID = orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    paymentDate = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_OPTIONS = (
        ('Credit', 'credit'),
        ('Debit', 'debit'),
        ('Cash', 'cash'),
    )
    paymentMethod = models.CharField(max_length=100, choices = PAYMENT_OPTIONS)
    
    def serialize(self):
        return {
            "paymentID": self.paymentID,
            "order": self.orderID.serialize(),
            "paymentDate": self.paymentDate.strftime("%Y-%m-%d %H:%M:%S"),
            "amount": str(self.amount),
            "paymentMethod": self.paymentMethod
        }
    
    def __str__(self):
        return f"Payment ID: {self.paymentID}"
    
class Shipping(models.Model):
    shippingID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipDate = models.DateTimeField()
    deliveryDate = models.DateTimeField()
    STATUS_OPTIONS = (
        ('Processing', 'processing'),
        ('Out for delivery', 'out for delivery'),
        ('Delivered', 'delivered'),
        ('Cancelled', 'cancelled')
    )
    status = models.CharField(max_length=100, choices = STATUS_OPTIONS)
    
    def serialize(self):
        return {
            "shippingID": self.shippingID,
            "order": self.orderID.serialize(),
            "shipDate": self.shipDate.strftime("%Y-%m-%d %H:%M:%S"),
            "deliveryDate": self.deliveryDate.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status
        }
        
    def __str__(self):
        return f"Shipping ID: {self.shippingID}"
    