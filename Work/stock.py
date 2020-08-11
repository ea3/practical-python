class Stock:
    # __slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        total_cost = self.shares * self.price
        return total_cost

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    def sell(self, shares_to_sell):
        self.shares = self.shares - shares_to_sell
        return self.shares

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
