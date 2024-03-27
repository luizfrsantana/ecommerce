from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

  
def home(request):
    return JsonResponse({"home": "home"})

def customer(request):
    return JsonResponse({"customer": "1"})

def customer_by_id(request):
    return JsonResponse({"customer_by_id": "customer_by_id_value"})

def product(request, ):
    return JsonResponse({"product": "product_value"})

def product_by_id(request):
    return JsonResponse({"product_by_id": "product_by_id_value"})

def order(request):
    return JsonResponse({"order": "order_value"})

def order_by_id(request):
    return JsonResponse({"order_by_id": "order_by_id_value"})

def order_details_by_order_by_id(request):
    return JsonResponse({"order_details_by_order_by_id": "order_details_by_order_by_id_value"})

def order_details_id_by_order_by_id(request):
    return JsonResponse({"order_details_id_by_order_by_id": "order_details_id_by_order_by_id_value"})

def category(request):
    return JsonResponse({"category": "category_value"})

def category_by_id(request):
    return JsonResponse({"category_by_id": "category_by_id_value"})

def payment(request):
    return JsonResponse({"payment_by_id": "payment_by_id_value"})

def payment_by_id(request):
    return JsonResponse({"payment_by_id": "payment_by_id_value"})

def payment_by_id(request):
    return JsonResponse({"payment_by_id": "payment_by_id_value"})

def shipping(request):
    return JsonResponse({"shipping": "shipping_value"})

def shipping_by_id(request):
    return JsonResponse({"shipping_by_id": "shipping_by_id_value"})


