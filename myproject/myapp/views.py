from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    templates_name = "list.html"
    model = Product
    paginate_by = 3