class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception

    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        from classes.customer import Customer
        return [*set([order.customer for order in self.orders()])]

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return sum([order.price for order in self.orders()])/ self.num_orders()
