import unittest2 as unittest

from classes.register import Register
from classes.trainer import Trainer


class TestTrainer(unittest.TestCase):

    def setUp(self):
        self.registers = [Register(1), Trainer(2)]

    def tearDown(self):
        pass

    def test_time_per_item(self):
        self.assertEqual(self.registers[1].time_per_item, 2)
