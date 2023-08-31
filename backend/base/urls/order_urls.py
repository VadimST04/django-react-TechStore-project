from django.urls import path
from base.views import order_views

urlpatterns = [
    path('add/', order_views.OrderAPIView.as_view(), name='orders-add'),
]
