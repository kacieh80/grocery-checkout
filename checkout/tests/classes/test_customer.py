import unittest2 as unittest

from classes.customer import Customer
from classes.register import Register
from classes.trainer import Trainer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_a1 = Customer('A', 1, 2)
        self.customer_a2 = Customer('A', 2, 1)
        self.customer_b1 = Customer('B', 1, 2)
        self.customer_b2 = Customer('B', 3, 1)
        self.registers = [Register(1), Trainer(2)]

    def tearDown(self):
        pass

    def test_find_register(self):
        """ Test different cases of find_register """
        self.customer_a1.find_register(self.registers)
        # Should be first customer in register 1
        self.assertEqual(self.registers[0].customers[0], self.customer_a1)

        self.customer_b1.find_register(self.registers)
        self.reset_registers()
        # Should be first customer in register 2
        self.assertEqual(self.registers[1].customers[0], self.customer_b1)

        self.customer_a2.find_register(self.registers)
        self.reset_registers()
        # Should be second customer in register 1
        self.assertEqual(self.registers[0].customers[1], self.customer_a2)

        self.customer_b2.find_register(self.registers)
        self.reset_registers()
        # Should be third customer in register 1
        self.assertEqual(self.registers[0].customers[2], self.customer_b2)

    def reset_registers(self):
        """ For clarity in the test we will put the registers
            back the way they were """
        self.registers.sort(key=lambda r: r.register_num)
