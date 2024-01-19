from django.urls import path

from products.views import product_list, product_details, product_create

urlpatterns = (
    path('', product_list, name='product list'),
    path('create/', product_create, name='product create'),
    path('<pk>/', product_details, name='product details')
)
