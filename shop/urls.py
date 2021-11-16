from django.urls import path
from . import views
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('delete-recipe/<int:pk>/', DeleteRecipeView.as_view(), name='delete-recipe'),
]
