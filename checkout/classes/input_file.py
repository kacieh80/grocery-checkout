""" Input File Class. Handles parsing the file and creating objects """


import sys

from classes.customer import Customer
from classes.register import Register
from classes.trainer import Trainer


class InputFile(object):

    def load_file(self, file_name):
        """ Given an input file, parse, store, and return it """
        try:
            data = open(file_name, 'r')
        except:
            print( 'Could not find your file.')
            sys.exit(-1)
        try:
            registers, customers = self._parse_file_data(data)
        except:
            print ('Something went wrong while parsing your file, \
                please check your file, and try again.')
            data.close()
            sys.exit(-1)
        data.close()

        return registers, customers

    def _parse_file_data(self, data):
        """ Parse the meat of the file and return registers and customers """
        customers = []

        for line in data:
            line_list = line.split(' ')
            # The first line is register count
            if len(line_list) <= 1:
                registers = self._get_registers(int(line_list[0].rstrip()))
            # Parse out customers data
            else:
                customer = Customer(line_list[0].rstrip(),  # type
                                    int(line_list[1].rstrip()),  # arrival
                                    int(line_list[2].rstrip()))  # items

                customers.append(customer)

        return registers, customers

    def _get_registers(self, register_count):
        """ Get a list of register objects and return them """
        registers = []

        for i in range(register_count):
            register_num = i + 1
            if register_count == (register_num):
                register = Trainer(register_num)
            else:
                register = Register(register_num)
            registers.append(register)

        return registers
