"""javed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
# from product.views import ProductListView, ProductDetailView, ProductDetailSlugView


from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from .views import home_page, about_page, contact_page, detail_page, login_page
# from account.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('product/', include("product.urls", namespace="product")),
    path('cart/', include("carts.urls", namespace="cart")),
    path('search/', include("search.urls", namespace="search")),
    # path('register/',register,name='register' ),
    # path('product/', ProductListView.as_view(), name="about"),
    # path('product/''<int:pk>', ProductDetailView.as_view(), name="about"),
    # path('product/''<slug:slug>', ProductDetailSlugView.as_view(), name="about"),
    path('contact/', contact_page, name="contact"),
    # path('detail/', detail_page, name="detail"),
    path('login/', login_page, name="login"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
