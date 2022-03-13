from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from products.models import Product
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

# Create your views here.
def manage_products(request):
    return render(request, 'products/products.html')

# Create your views here.
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductView(ListView):
    model = Product
    template_name = "products/products_list.html"    

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCreate(CreateView):
    model = Product
    fields = ['category','title','description','price','quantity','sku','picture']
    success_url = reverse_lazy('products_list')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    fields = ['category','title','description','price','quantity','sku','picture']
    success_url = reverse_lazy('products_list')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products_list')
