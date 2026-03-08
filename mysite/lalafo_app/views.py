from django.urls import reverse_lazy
from .models import Category, Product
from django.views.generic import (ListView, CreateView,
                                  DetailView, UpdateView,
                                  DeleteView)
from .forms import ProductForm


class MarchListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'C'
    template_name = 'march8.html'


class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'category_list.html'


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
