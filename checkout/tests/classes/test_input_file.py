import unittest2 as unittest

from classes.customer import Customer
from classes.input_file import InputFile
from classes.register import Register


class TestInputFile(unittest.TestCase):

    def setUp(self):
        self.input_file = InputFile()

    def tearDown(self):
        pass

    def test_load_file(self):
        f = "input_files/example2.txt"
        registers, customers = self.input_file.load_file(f)
        self.assertEqual(type(registers[0]), Register)
        self.assertEqual(type(customers[0]), Customer)
