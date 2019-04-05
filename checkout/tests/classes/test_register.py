import unittest2 as unittest

from classes.customer import Customer
from classes.register import Register
from classes.trainer import Trainer


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.customer_a1 = Customer('A', 1, 2)
        self.customer_a2 = Customer('A', 2, 1)
        self.customer_b1 = Customer('B', 1, 2)
        self.registers = [Register(1), Trainer(2)]
        self.registers[0].customers.append(self.customer_a1)
        self.registers[0].customers.append(self.customer_a2)
        self.registers[0].customers.append(self.customer_b1)

    def tearDown(self):
        pass

    def test_time_per_item(self):
        self.assertEqual(self.registers[0].time_per_item, 1)

    def test_get_customer_count(self):
        self.assertEqual(self.registers[0].get_customer_count(), 3)
        self.assertEqual(self.registers[1].get_customer_count(), 0)

    def test_get_last_customer(self):
        self.assertEqual(self.registers[0].get_last_customer(),
                         self.customer_b1)

    def test_get_checkout_time(self):
        self.assertEqual(self.registers[0].get_checkout_time(), 6)

    def reset_registers(self):
        """ For clarity in the test we will put the registers
            back the way they were """
        self.registers.sort(key=lambda r: r.register_num)
