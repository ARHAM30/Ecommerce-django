from .views import cart_home, update_cart
from django.urls import path

app_name = 'cart'
urlpatterns = [
    path('', cart_home, name="home"),
    path('update', update_cart, name="update"),
]
