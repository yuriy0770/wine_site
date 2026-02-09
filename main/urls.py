from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoriesList.as_view(), name='categories'),
    path('categories/<slug:category_slug>/', views.CategoriesDetail.as_view(), name='detail'),
    path('product/<slug:product_slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('about/', views.about, name='about'),
]
