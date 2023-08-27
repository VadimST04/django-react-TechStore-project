from django.urls import path
from base.views import product_views

urlpatterns = [
    path('', product_views.ProductView.as_view(), name='products'),
    path('<str:pk>/', product_views.ProductView.as_view(), name='products'),
]