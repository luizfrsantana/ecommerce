from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    path('', views.home),

    #Customer Paths
    path('customer', views.url_customer), 
    path('customer/<int:customerID>', views.url_customer_by_id),

    #Customer Paths
    path('product', views.url_product), 
    path('product/<int:productID>', views.url_product_by_id),
    
    #Order Paths
    path('order/', views.url_order), 
    path('order/<int:orderID>', views.url_order_by_id),
    path('order/<int:orderID>/iten', views.url_order_details_by_order_by_id),
    path('order/<int:orderID>/iten/<int:orderDetailID>', views.url_order_details_id_by_order_by_id),
    
    #Category Paths
    path('category', views.url_category),
    path('category/<int:categoryID>', views.url_category_by_id),
    
    #Payment Paths
    path('payment', views.url_payment),
    path('payment/<int:paymentID>', views.url_payment_by_id),
    
    #Shipping Paths
    path('shipping', views.url_payment),
    path('shipping/<int:shippingID>', views.url_shipping_by_id),
]