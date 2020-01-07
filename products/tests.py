from django.test import TestCase
from .models import Product

class ProductTest(TestCase):
    """
    Test for the Product class in the Product model
    """
    def test_str(self):
        test_name = Product(name='A product')
        self. assertEqual(str(test_name), 'A product')