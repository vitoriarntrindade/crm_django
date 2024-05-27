from django.shortcuts import get_object_or_404
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
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


class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def form_valid(self, form):
        return super().form_valid(form=form)

    def get_success_url(self):
        return reverse("customer:customer-list")


class CustomerDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def get_success_url(self):
        return reverse("customer:customer-list")