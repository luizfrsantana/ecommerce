from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    path('', views.home),

    #Customer Paths
    path('customer', views.customer), 
    path('customer/<int:customerID>', views.customer_by_id),

    #Customer Paths
    path('product', views.product), 
    path('product/<int:productID>', views.product_by_id),
    
    #Order Paths
    path('order/', views.order), 
    path('order/<int:orderID>', views.order_by_id),
    path('order/<int:orderID>/iten', views.order_details_by_order_by_id),
    path('order/<int:orderID>/iten/<int:orderDetailID>', views.order_details_id_by_order_by_id),
    
    #Category Paths
    path('category', views.category),
    path('category/<int:categoryID>', views.category_by_id),
    
    #Payment Paths
    path('payment', views.payment),
    path('payment/<int:paymentID>', views.payment_by_id),
    
    #Shipping Paths
    path('shipping', views.payment),
    path('shipping/<int:shippingID>', views.shipping_by_id),
]