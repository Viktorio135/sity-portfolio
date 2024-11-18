from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.


class PagesTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('main:index_page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


