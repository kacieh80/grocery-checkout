import unittest2 as unittest

from classes.checkout import Checkout
from classes.customer import Customer
from classes.register import Register
from classes.trainer import Trainer


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.customers = [Customer('A', 1, 2),
                          Customer('A', 2, 1),
                          Customer('B', 1, 2),
                          Customer('B', 3, 1)]
        self.registers = [Register(1), Trainer(2)]
        self.checkout = Checkout(self.customers, self.registers)

    def tearDown(self):
        pass

    def test_assign_registers(self):
        self.checkout.assign_registers()
        self.registers.sort(key=lambda r: r.register_num)
        # We check the registers customers attribute to ensure it worked
        self.assertEqual(len(self.registers[0].customers), 3)
        self.assertEqual(len(self.registers[1].customers), 1)

    def test_run_checkout(self):
        self.checkout.assign_registers()
        self.assertEqual(self.checkout.run_checkout(), 5)
