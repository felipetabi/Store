from django.shortcuts import render

from django.views.generic.list import ListView
from products.models import Product
from django.views.generic.detail import DetailView

class ProductListView(ListView):
    template_name = 'index.html' 
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Productos'
        context['products'] = context['product_list']

        return context

class ProductDetailView(DetailView):
    model =  Product
    template_name ='products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        return Product.objects.filter(title=self.query())

    def query(self):
        return self.request.GET.get('q')
