from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('pt/', views.pt,  name='pt'),
    path('nutrition/', views.nutrition,  name='nutrition'),
    path('gymgear/', views.gymgear,  name='gymgear'),
]
