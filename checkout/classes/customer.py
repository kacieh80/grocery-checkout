""" Customer class """


class Customer(object):

    def __init__(self, cust_type, arrival_time, items):
        self.cust_type = cust_type
        self.arrival_time = arrival_time
        self.num_of_items = items

    def find_register(self, registers):
        """ Find register to insert self into (does not return anything) """
        if self.cust_type.upper() == 'A':
            self._find_type_a_register(registers)
        # Default type B
        else:
            self._find_type_b_register(registers)

    def _find_type_b_register(self, registers):
        """ Find register per type B logic (does not return anything) """
        registers.sort(key=lambda r: r.get_customer_count())
        if registers[0].get_customer_count() != 0:
            position = self._position_of_register_type_b(registers)
            registers[position].customers.append(self)
        else:
            registers[0].customers.append(self)

    def _find_type_a_register(self, registers):
        """ Find register per type A logic (does not return anything) """
        registers.sort(key=lambda r: (r.get_customer_count(), r.register_num))
        if registers[0].get_customer_count() != 0:
            # Check if any customers have left
            position = self._position_of_register_type_a(registers)
            registers[position].customers.append(self)
        else:
            registers[0].customers.append(self)

    def _position_of_register_type_b(self, registers):
        """ Find the postion in the register list for type B and return it """
        position = 0
        cust_items_list = []
        for r in registers:
            cust_items = r.get_last_customer().num_of_items
            cust_items_list.append({'items': cust_items, 'position': position})
            position = position + 1
        cust_items_list.sort(key=lambda i: i['items'])
        return cust_items_list[0]['position']

    def _position_of_register_type_a(self, registers):
        """ Find the postion in the register list for type A and return it """
        position = 0
        customer_count_list = []
        for r in registers:
            cust_count_dict = {'position': position, 'count': 0}
            for c in r.customers:
                if (c.num_of_items * r.time_per_item) >= self.arrival_time:
                    cust_count_dict['count'] = cust_count_dict['count'] + 1
            customer_count_list.append(cust_count_dict)
            position = position + 1
        customer_count_list.sort(key=lambda cc: cc['count'])
        return customer_count_list[0]['position']
