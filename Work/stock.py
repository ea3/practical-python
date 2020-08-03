class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        total_cost = self.shares * self.price
        return total_cost

    def sell(self, shares_to_sell):
        self.shares = self.shares - shares_to_sell

        return self.shares
