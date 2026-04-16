from django.test import TestCase
from .models import Menu, Booking
from datetime import date
from decimal import Decimal

# Create your tests here.
class MenuItemTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Pasta", price=Decimal('10.99'), inventory=5)
        Menu.objects.create(name="Pizza", price=Decimal('8.99'), inventory=3)

    def test_menu_item_creation(self):
        pasta = Menu.objects.get(name="Pasta")
        pizza = Menu.objects.get(name="Pizza")
        self.assertEqual(pasta.price, Decimal('10.99'))
        self.assertEqual(pizza.inventory, 3)

class BookingTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(first_name="John Doe", reservation_date=date(2024, 7, 1), reservation_slot=19, no_of_guests=4)
        Booking.objects.create(first_name="Jane Smith", reservation_date=date(2024, 7, 2), reservation_slot=20, no_of_guests=2)

    def test_booking_creation(self):
        john = Booking.objects.get(first_name="John Doe")
        jane = Booking.objects.get(first_name="Jane Smith")
        self.assertEqual(john.no_of_guests, 4)
        self.assertEqual(jane.reservation_date, date(2024, 7, 2))