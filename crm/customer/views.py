from django.views.generic import ListView, CreateView
from .forms import CustomerForm
from .models import Customer
from django.urls import reverse


class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()


class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    model = Customer
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form=form)

    def get_success_url(self):
        return reverse("customer:customer-list")