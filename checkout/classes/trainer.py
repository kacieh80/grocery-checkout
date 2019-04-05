""" Trainer class, we might need more here some day """


from classes.register import Register


class Trainer(Register):

    def __init__(self, register_num):
        super(Trainer, self).__init__(register_num)
        self.time_per_item = 2
