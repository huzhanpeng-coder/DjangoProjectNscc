from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from categories.models import Category
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoriesView(ListView):
    model = Category
    template_name = "categories/categories_list.html"
    
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories_list')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories_list')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categories_list')    


