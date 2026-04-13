from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_menu_str(self):
        item = Menu.objects.create(title="IceCream", price=80, description="Vanilla", is_available=True)
        self.assertEqual(str(item), "IceCream : 80")
