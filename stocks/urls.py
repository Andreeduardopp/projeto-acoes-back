from django.urls import path
from .views import get_stock_prices

urlpatterns = [
    path('stocks/', get_stock_prices, name='get_stock_prices'), 
    path('stocks/<str:ticker>/', get_stock_prices, name='get_stock_prices_path'),  
]
