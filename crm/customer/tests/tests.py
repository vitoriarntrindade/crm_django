from django.test import TestCase
from django.urls import reverse
from customer.models import Customer


class TestViewsCustomer(TestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(
            first_name='Carlos', last_name='Silva', email='carlos.silva@gmail.com',
            birth_date='1990-01-01', area_code='21', phone_number='987654321',
            country='Brasil', state='RJ', city='Rio de Janeiro'
        )
        self.customer2 = Customer.objects.create(
            first_name='Maria', last_name='Oliveira', email='maria.oliveira@hotmail.com',
            birth_date='1992-02-02', area_code='11', phone_number='987654322',
            country='Brasil', state='SP', city='São Paulo'
        )
        self.customer3 = Customer.objects.create(
            first_name='José', last_name='Santos', email='jose.santos@bol.com',
            birth_date='1985-03-03', area_code='31', phone_number='987654323',
            country='Brasil', state='MG', city='Belo Horizonte'
        )

    def test_list_customers(self):
        response = self.client.get(reverse('customer:customer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/customer_list.html')
        self.assertContains(response, self.customer1.first_name)
        self.assertContains(response, self.customer2.first_name)
        self.assertContains(response, self.customer3.first_name)

    def test_list_customers_search(self):
        response = self.client.get(reverse('customer:customer-list'), {'name': 'Maria'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.customer1.first_name)
        self.assertContains(response, self.customer2.first_name)
        self.assertNotContains(response, self.customer3.first_name)

    def test_update_customer(self):
        response = self.client.get(reverse('customer:customer-update', kwargs={'id': self.customer1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/customer.html')

        self.customer1.first_name = "José"
        self.customer1.email = "emaildojose@hotmail.com"
        self.customer1.save()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.customer1.first_name, 'José')
        self.assertEqual(self.customer1.email, 'emaildojose@hotmail.com')

    def test_delete_customer(self):
        response = self.client.post(reverse('customer:customer-delete', kwargs={'id': self.customer2.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Customer.objects.filter(id=self.customer2.id).exists())

