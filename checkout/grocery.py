""" grocery.py """


import sys

from classes.input_file import InputFile
from classes.checkout import Checkout


if len(sys.argv) == 1:
    print('Please provide a filename.')
    sys.exit(-1)

registers, customers = InputFile().load_file(sys.argv[1])
checkout = Checkout(customers, registers)
checkout.assign_registers()
t = checkout.run_checkout()

print('Finished at: t={time} minutes'.format(time=t))
sys.exit(-1)
