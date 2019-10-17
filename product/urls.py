

from .views import ProductListView, ProductDetailSlugView
from django.urls import path

app_name='product'
urlpatterns = [
    path('', ProductListView.as_view(), name="about"),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name="slug"),
]
