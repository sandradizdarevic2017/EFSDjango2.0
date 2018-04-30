from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Sum
from rest_framework.views import APIView
from .serializers import CustomerSerializer
from rest_framework.response import Response


from . models import Customer, Investment, Stock


class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'


class CustomerListView(LoginRequiredMixin,ListView):
    model = Customer
    fields = '__all__'
    template_name = 'customer_list.html'
    login_url = 'login'


class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    model = Customer
    fields = ['name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'cell_phone']
    template_name = 'customer_edit.html'
    login_url = 'login'

class CustomerDeleteView(LoginRequiredMixin,DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('home')



class InvestmentListView(LoginRequiredMixin,ListView):
    model = Investment
    fields = '__all__'
    login_url = 'login'
    template_name = 'investment_list.html'


class InvestmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Investment
    fields = '__all__'
    login_url = 'login'
    template_name = 'investment_edit.html'

class InvestmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Customer
    template_name = 'investment_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

class StockListView(LoginRequiredMixin,ListView):
    model = Stock
    fields = '__all__'
    login_url = 'login'
    template_name = 'stock_list.html'

class StockUpdateView(LoginRequiredMixin,UpdateView):
    model = Stock
    fields = '__all__'
    login_url = 'login'
    template_name = 'stock_edit.html'

class StockDeleteView(LoginRequiredMixin,DeleteView):
    model = Stock
    template_name = 'stock_delete.html'
    success_url = reverse_lazy('home')



class PortfolioListView(ListView):

    def get_queryset(self):
        return Customer.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        customer = self.get_queryset()[0]

        context = super(PortfolioListView, self).get_context_data(**kwargs)
        investments = Investment.objects.filter(customer=customer)
        stocks = Stock.objects.filter(customer=customer)
        sum_acquired_value = Investment.objects.filter(customer=customer).aggregate(Sum('acquired_value'))['acquired_value__sum']
        sum_recent_value = Investment.objects.filter(customer=customer).aggregate(Sum('recent_value'))['recent_value__sum']

        sum_current_stocks_value = 0
        sum_of_initial_stock_value = 0

        for stock in stocks:
            sum_current_stocks_value += stock.current_stock_value()
            sum_of_initial_stock_value += stock.initial_stock_value()
        context['stocks'] = stocks
        context['investments'] = investments
        context['sum_current_stocks_value'] = sum_current_stocks_value
        context['sum_of_initial_stock_value'] = sum_of_initial_stock_value
        context['result'] = sum_current_stocks_value - sum_of_initial_stock_value
        context['sum_acquired_value'] = sum_acquired_value
        context['sum_recent_value'] = sum_recent_value
        context['result_investment'] = sum_recent_value - sum_acquired_value
        return context

    template_name = 'portfolio_list.html'

class CustomerList(APIView):
    def get(self, request):
        customers_json = Customer.objects.all()
        serializer = CustomerSerializer(customers_json, many=True)
        return Response(serializer.data)









