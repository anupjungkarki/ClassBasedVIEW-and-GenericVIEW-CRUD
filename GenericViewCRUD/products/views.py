from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Product
from .forms import ProductForm


# Create your views here.
class CreateProductView(CreateView):
    model = Product
    # fields = ['name', 'slug', 'description', 'image', 'price']
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/list/'


class ListProductView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class UpdateProductView(UpdateView):
    model = Product
    fields = ['name', 'slug', 'description', 'image', 'price']
    template_name = 'product_form.html'
    success_url = '/list/'


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = '/list/'

class ProductShowView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'item'

