from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic as views

def product_list(request):
    return render(request, 'products/products.html')


def product_details(request, pk):
    return render(request, 'products/product-detail.html')


@login_required
class ProductCreate(views.CreateView):