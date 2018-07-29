from datetime import datetime
from django.test import TestCase
from django.utils import dateformat
from olegsshop import settings
from .models import Basket
from authapp.models import ShopUser
from mainapp.models import Product, Category


# Create your tests here.
class Test_Basket(TestCase):

    def setUp(self):
        self.test_User = ShopUser(age='23')
        self.test_User.save()
        self.test_Product = Product(name='test_name', desc='test_desk', desc_full='test_desk_full', price=33,
                                    price_low=21, count=44, image='test_image')
        self.test_Product.save()
        self.basket = Basket(user=self.test_User, product=self.test_Product, quantity=2)
        self.basket.save()

        def tearDown(self):
            pass

    def test__get_product_cost(self):
        self.assertEqual(self.basket.get_product_cost(), 66)

    def test__get_totalquantity(self):
        self.assertEqual(self.basket.get_totalquantity(), 2)

    def test__get_totalcost(self):
        self.assertEqual(self.basket.get_totalcost(), 66)


