""" Checkout Class """


class Checkout(object):

    def __init__(self, customers, registers):
        self.customers = customers
        self.registers = registers

    def assign_registers(self):
        """ Assign customers to registers (no return value) """
        self.customers.sort(key=lambda x: x.arrival_time)
        for c in self.customers:
            c.find_register(self.registers)

    def run_checkout(self):
        """ Check everyone out and retrun the time it took """
        checkout_mins = []
        for r in self.registers:
            checkout_mins.append(r.get_checkout_time())

        checkout_mins.sort()
        return checkout_mins[-1]
