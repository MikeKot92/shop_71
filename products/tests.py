from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('products:home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Home')
        self.assertTemplateUsed(response, 'index.html')


class ProductListViewTestCase(TestCase):
    fixtures = ['categories.json', 'products.json',]

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:catalog')
        response = self.client.get(path)
        self._common_test(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.products[:6]))

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)
        self._common_test(response)
        self.assertEqual(list(response.context_data['object_list']),
                         list(self.products.filter(category_id=category.id)))

    def _common_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Catalog')
        self.assertTemplateUsed(response, 'catalog.html')
