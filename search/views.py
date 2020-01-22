from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product
from django.db.models import Q

class SearchProductView(ListView):
    # queryset = Product.objects.all()
    template_name = "search/view.html"
    def  get_queryset(self,*args,**kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(tag__title__icontains=query)
            return Product.objects.filter(lookups).distinct()
        return Product.objects.none()
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
