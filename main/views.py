from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Category


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
