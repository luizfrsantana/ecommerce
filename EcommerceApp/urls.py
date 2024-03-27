from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    path('', views.home, name='home'),
    
    #Customer Paths
    path('customer/', views.customer, name='customer'), 
    path('customer/<int:customerID>', views.customer_by_id, name='customer_by_id'),
    
    #Customer Paths
    path('product/', views.product, name='product'), 
    path('product/<int:productID>', views.product_by_id, name='product_by_id')
    
    #Order Paths
    path('order/', views.order, name='order'), 
    path('order/<int:orderID>', views.order_by_id, name='order_by_id')
    path('order/<int:orderID>/iten', views.order_details_by_order_by_id, name='order_details_by_order_by_id')
    path('order/<int:orderID>/iten/<int:orderDetailID>', views.order_details_id_by_order_by_id, name='order_details_id_by_order_by_id')
    
    #Category Paths
    path('category/', views.category, name='category'),
    path('category/<int:categoryID>', views.category_by_id, name='category_by_id')
    
    #Payment Paths
    path('payment/', views.payment, name='payment'),
    path('payment/<int:paymentID>', views.payment_by_id, name='payment_by_id')
    
    
    #Shipping Paths
    path('shipping/', views.payment, name='shipping'),
    path('shipping/<int:shippingID>', views.shipping_by_id, name='shipping_by_id')
    
]