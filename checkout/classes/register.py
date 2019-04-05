""" Register Class """


class Register(object):

    def __init__(self, register_num):
        self.customers = []
        self.register_num = register_num
        self.time_per_item = 1

    def get_customer_count(self):
        """ Returns the number of customers that the register will serve """
        return len(self.customers)

    def get_last_customer(self):
        """ Returns the last customer to be served """
        return self.customers[-1]

    def get_checkout_time(self):
        """ Returns the total checkout time for a register """
        total_items = 0
        for c in self.customers:
            total_items = total_items + c.num_of_items

        return (total_items * self.time_per_item) + 1
