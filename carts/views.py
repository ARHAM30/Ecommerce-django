from django.shortcuts import render, redirect

from product.models import Product
from .models import Cart

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart": cart_obj})

def update_cart(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("show user the message that, the product has been gone!")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.product.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.product.add(product_obj)
        # return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")
