from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Customer, Category, Product, Payment, Order, Shipping, OrderDetails

# Create your views here.
 
def home(request):
    return JsonResponse({"home": "home"})

#### CUSTOMER ###

def url_customer(request):
    if request.method == 'POST':
       if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            return create_customer(data)       
    elif request.method == 'GET':
        page_number = request.GET.get('page_number')
        page_size = request.GET.get('page_size')
        if page_number and page_size:
            return list_customers(page_number,page_size)
        else:
            return list_customers()

def url_customer_by_id(request, customerID):
    if request.method == 'DELETE':
        return delete_customer_by_id(customerID)
        
    elif request.method == 'PUT':
        data = json.loads(request.body)
        return update_customer_by_id(customerID, data)
        
    elif request.method == 'GET':
        if 'application/json' in request.content_type: 
            return find_customer(customerID)

def list_customers(page_number=None, page_size=None ):
    if (page_number or page_size) is None:
        #return all customers
        customers = Customer.objects.all()

    else:
        #return some customers
        start = (int(page_number) - 1) * int(page_size)
        end = start + int(page_size)
        customers = Customer.objects.all() [start:end]
        
    customers_data = []
    for customer in customers:
        customers_data.append(customer.serialize())
    return JsonResponse(customers_data, safe=False, status=200)        

def create_customer(data):
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')
    new_customer = Customer(name=name,email=email, phone=phone, address=address)
    new_customer.save()
    return JsonResponse({"Customer created": new_customer.serialize()}, status=200)

def find_customer(customerID):
    customer = Customer.objects.get(customerID=customerID)
    return JsonResponse({"Customer Solicited": customer.serialize()}, status=200)

def delete_customer_by_id(customerID):
    customer = Customer.objects.get(customerID=customerID)
    customer.delete()
    return JsonResponse({"Customer Deleted": "Sucess"}, status=200)

def update_customer_by_id(customerID, data):
    customer = Customer.objects.get(customerID=customerID)
    customer.name = data.get('name')
    customer.email = data.get('email')
    customer.phone = data.get('phone')
    customer.address = data.get('address')
    customer.save()
    return JsonResponse({"Customer Updated": customer.serialize()}, status=200)

#### PRODUCT ###

def url_product(request):
    if request.method == 'POST':
       if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            return create_product(data)       
    elif request.method == 'GET':    
        return all_products()

def url_product_by_id(request, productID):
    if request.method == 'DELETE':
        return delete_product_by_id(productID)
        
    elif request.method == 'PUT':
        data = json.loads(request.body)
        if 'application/json' in request.content_type:
            return update_product_by_id(productID, data)
        
    elif request.method == 'GET':
        return find_product(productID)

def all_products():
    products = Product.objects.all()
    products_data = []
    for product in products:
        products_data.append(product.serialize())
    return JsonResponse(products_data, safe=False, status=200)

def create_product(data):
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    stock = data.get('stock')
    category_id = data.get('categoryID')
    category = Category.objects.get(pk=category_id)
    new_product = Product(name=name, price=price, description=description, stock=stock, categoryID=category)
    new_product.save()
    return JsonResponse({"Product created": new_product.serialize()}, status=200)

def find_product(productID):
    product = Product.objects.get(productID=productID)
    return JsonResponse({"Product Solicited": product.serialize()}, status=200)

def delete_product_by_id(productID):
    product = Product.objects.get(productID=productID)
    product.delete()
    return JsonResponse({"Product Deleted": "Success"}, status=200)

def update_product_by_id(productID, data):
    product = Product.objects.get(productID=productID)
    product.name = data.get('name')
    product.price = data.get('price')
    product.description = data.get('description')
    product.stock = data.get('stock')
    category_id = data.get('categoryID')
    category = Category.objects.get(pk=category_id)
    product.categoryID = category
    product.save()
    return JsonResponse({"Product Updated": product.serialize()}, status=200)
    
#### CATEGORY ###

def url_category(request):
    if request.method == 'POST':
       if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            return create_category(data)       
    elif request.method == 'GET':    
        return all_categories()

def url_category_by_id(request, categoryID):
    if request.method == 'DELETE':
        return delete_category_by_id(categoryID)
        
    elif request.method == 'PUT':
        data = json.loads(request.body)
        return update_category_by_id(categoryID, data)
        
    elif request.method == 'GET':
        return find_category(categoryID)

def all_categories():
    categories = Category.objects.all()
    categories_data = []
    for category in categories:
        categories_data.append(category.serialize())
    return JsonResponse(categories_data, safe=False, status=200)

def create_category(data):
    name = data.get('name')
    description = data.get('description')
    new_category = Category(name=name, description=description)
    new_category.save()
    return JsonResponse({"Category created": new_category.serialize()}, status=200)
    
def find_category(categoryID):
    category = Category.objects.get(categoryID=categoryID)
    return JsonResponse({"Category Solicited": category.serialize()}, status=200)

def delete_category_by_id(categoryID):
    category = Category.objects.get(categoryID=categoryID)
    category.delete()
    return JsonResponse({"Category Deleted": "Success"}, status=200)

def update_category_by_id(categoryID, data):
    category = Category.objects.get(categoryID=categoryID)
    category.name = data.get('name')
    category.description = data.get('description')
    category.save()
    return JsonResponse({"Category Updated": category.serialize()}, status=200)

### PAYMENTS ###

def url_payment(request):
    if request.method == 'POST':
       if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            return create_payment(data)       
    elif request.method == 'GET':    
        return all_payments()

def url_payment_by_id(request, paymentID):
    if request.method == 'DELETE':
        return delete_payment_by_id(paymentID)
        
    elif request.method == 'PUT':
        data = json.loads(request.body)
        return update_payment_by_id(paymentID, data)
        
    elif request.method == 'GET':
        return find_payment(paymentID)

def all_payments():
    payments = Payment.objects.all()
    payments_data = []
    for payment in payments:
        payments_data.append(payment.serialize())
    return JsonResponse(payments_data, safe=False, status=200)

def create_payment(data):
    orderID = data.get('orderID')
    paymentDate = data.get('paymentDate')
    amount = data.get('amount')
    paymentMethod = data.get('paymentMethod')
    
    order = Order.objects.get(pk=orderID)
    
    new_payment = Payment(orderID=order, paymentDate=paymentDate, amount=amount, paymentMethod=paymentMethod)
    new_payment.save()
    return JsonResponse({"Payment created": new_payment.serialize()}, status=200)

def find_payment(paymentID):
    payment = Payment.objects.get(paymentID=paymentID)
    return JsonResponse({"Payment Solicited": payment.serialize()}, status=200)

def delete_payment_by_id(paymentID):
    payment = Payment.objects.get(paymentID=paymentID)
    payment.delete()
    return JsonResponse({"Payment Deleted": "Success"}, status=200)

def update_payment_by_id(paymentID, data):
    payment = Payment.objects.get(paymentID=paymentID)
    payment.orderID = data.get('orderID')
    payment.paymentDate = data.get('paymentDate')
    payment.amount = data.get('amount')
    payment.paymentMethod = data.get('paymentMethod')
    payment.save()
    return JsonResponse({"Payment Updated": payment.serialize()}, status=200)

### ORDER ###

def url_order(request):
    if request.method == 'POST':
       if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            return create_order(data)       
    elif request.method == 'GET':    
        return all_orders()

def url_order_by_id(request, orderID):
    if request.method == 'DELETE':
        return delete_order_by_id(orderID)
        
    elif request.method == 'GET':
        return find_order(orderID)

def all_orders():
    orders = Order.objects.all()
    orders_data = []
    for order in orders:
        orders_data.append(order.serialize())
    return JsonResponse(orders_data, safe=False, status=200)

def create_order(data):
    customerID = data.get('customerID')
    customer = Customer.objects.get(pk=customerID)
    
    new_order = Shipping(customerID=customer)
    new_order.save()
    return JsonResponse({"Shipping created": new_order.serialize()}, status=200)

def find_order(orderID):
    order = Order.objects.get(orderID=orderID)
    return JsonResponse({"Order Solicited": order.serialize()}, status=200)

def delete_order_by_id(orderID):
    order = Order.objects.get(orderID=orderID)
    order.delete()
    return JsonResponse({"Order deleted":"Success"}, status=200)

### ORDER DETAILS ###

def url_order_details_by_order_by_id(request, orderID):
    if request.method == 'POST':
       if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            return create_order_details(data,orderID)       
    elif request.method == 'GET':    
        return all_one_order_details(orderID)
    
def url_order_details_id_by_order_by_id(request, orderID, orderDetailID):
    order = Order.objects.get(orderID=orderID)
    orderDetails = OrderDetails.objects.get(orderID=order)
    return JsonResponse({"Order Details Solicited": orderDetails.serialize()}, status=200)

def all_one_order_details(orderID):
    order = Order.objects.get(orderID=orderID)
    orderDetails = OrderDetails.objects.get(orderID=order)
    return JsonResponse({"Order Details Solicited": orderDetails.serialize()}, status=200)

def create_order_details(data, orderID):
    productID = data.get('productID')
    quantity = data.get('quantity')
    
    order = Order.objects.get(orderID=orderID)
    product = Product.objects.get(productID=productID)
    
    new_order_details = OrderDetails(orderID=order, productID=product, quantity=quantity)
    new_order_details.save()
    
    return JsonResponse({"Order Details created": new_order_details.serialize()}, status=200)

def update_order_details_by_id(orderDetailID, data):
    order_details = OrderDetails.objects.get(orderDetailID=orderDetailID)
    order_details.productID = data.get('productID')
    order_details.quantity = data.get('quantity')
    order_details.save()
    return JsonResponse({"Order Details Updated": order_details.serialize()}, status=200)

def delete_order_details_by_id(orderDetailID):
    order_details = OrderDetails.objects.get(orderDetailID=orderDetailID)
    order_details.delete()
    return JsonResponse({"Order Details Deleted": "Success"}, status=200)

def find_order_details_by_id(orderDetailID):
    order_details = OrderDetails.objects.get(orderDetailID=orderDetailID)
    return JsonResponse({"Order Details Solicited": order_details.serialize()}, status=200)

### SHIPPING ###
def url_shipping(request):
    if request.method == 'POST':
       if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            return create_shipping(data)       
    elif request.method == 'GET':    
        return all_shippings()

def url_shipping_by_id(request, shippingID):
    if request.method == 'DELETE':
        return delete_shipping_by_id(shippingID)
        
    elif request.method == 'PUT':
        data = json.loads(request.body)
        return update_shipping_by_id(shippingID, data)
        
    elif request.method == 'GET':
        return find_shipping(shippingID)

def all_shippings():
    shippings = Shipping.objects.all()
    shippings_data = []
    for shipping in shippings:
        shippings_data.append(shipping.serialize())
    return JsonResponse(shippings_data, safe=False, status=200)

def create_shipping(data):
    orderID = data.get('orderID')
    shipDate = data.get('shipDate')
    deliveryDate = data.get('deliveryDate')
    status = data.get('status')
    
    order = Order.objects.get(pk=orderID)
    
    new_shipping = Shipping(orderID=order, shipDate=shipDate, deliveryDate=deliveryDate, status=status)
    new_shipping.save()
    return JsonResponse({"Shipping created": new_shipping.serialize()}, status=200)

def find_shipping(shippingID):
    shipping = Shipping.objects.get(shippingID=shippingID)
    return JsonResponse({"Shipping Solicited": shipping.serialize()}, status=200)

def delete_shipping_by_id(shippingID):
    shipping = Shipping.objects.get(shippingID=shippingID)
    shipping.delete()
    return JsonResponse({"Shipping Deleted": "Success"}, status=200)

def update_shipping_by_id(shippingID, data):
    shipping = Shipping.objects.get(shippingID=shippingID)
    shipping.orderID = data.get('orderID')
    shipping.shipDate = data.get('shipDate')
    shipping.deliveryDate = data.get('deliveryDate')
    shipping.status = data.get('status')
    shipping.save()
    return JsonResponse({"Shipping Updated": shipping.serialize()}, status=200)



