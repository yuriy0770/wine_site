from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Category, Product


def index(request):
    return render(request, 'main/index.html')

class CategoriesList(ListView):
    model = Category
    context_object_name = 'category'


class CategoriesDetail(DetailView):
    model = Category
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['con'] = self.object.products.all()
        return context

def about(request):
    return render(request, 'main/about.html')


class ProductDetail(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Можно добавить связанные товары или другие данные
        return context
