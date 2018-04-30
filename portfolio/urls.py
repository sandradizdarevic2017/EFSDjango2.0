from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),

    path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/edit/',
        views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer/<int:pk>/delete/',
        views.CustomerDeleteView.as_view(), name='customer_delete'),

    path('investment_list/', views.InvestmentListView.as_view(), name='investment_list'),
    path('investment/<int:pk>/edit/',
        views.InvestmentUpdateView.as_view(), name='investment_edit'),
    path('investment/<int:pk>/delete/',
        views.InvestmentDeleteView.as_view(), name='investment_delete'),


    path('stock_list/', views.StockListView.as_view(), name='stock_list'),
    path('stock/<int:pk>/edit/',
        views.StockUpdateView.as_view(), name='stock_edit'),
    path('stock/<int:pk>/delete/',
        views.StockDeleteView.as_view(), name='stock_delete'),


    path('portfolio/<int:pk>/customer/', views.PortfolioListView.as_view(), name='portfolio_list'),
    path('customers_json/' , views.CustomerList.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
