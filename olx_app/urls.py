from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('c_product', views.c_product, name='c_product'),
    path('register', views.register, name='register' ),
    path('login/', views.register, name='login' ),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete_post, name='delete'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('category/', views.category_detail, name='category_detail' ),
    path('search/', views.search, name='search_results'),
    path('favourite', views.favourite, name='favourite'),
    path('favourite/add/<int:product_id>', views.add_to_favourite, name='add_to_favourite'),
    path('favourite/delete/<int:product_id>', views.delete_favourite, name='delete_favourite'),
    ]