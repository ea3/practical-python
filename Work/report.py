import csv
from pprint import pprint


# def read_portfolio(filename):
#
#     """ Computes the total cost (shares*price) of a portfolio file """
#
#     with open(filename, 'rt') as rows:
#         header = next(rows)
#         print(header)
#         for row in rows:
#             line = row.split(',')
#             holding = (line[0], int(line[1]), float(line[2]))
#             portfolio.append(holding)
#         return portfolio
#
#
# cost = read_portfolio('Data/portfolio.csv')
# print(cost)

# Now as a dictionary:


def read_portfolio(filename):

    """ Computes the total cost (shares*price) of a portfolio file """

    with open(filename, 'rt') as file:

        portfolio = []
        header = next(file)
        total = 0
        for line in file:
            line2 = line.split(',')
            # total += (int(line2[1])) * (float(line2[2]))
            # print((int(line2[1])))
            # print((float(line2[2])))
            dictionary_stocks = {'name': line2[0],
                                 'shares': int(line2[1]),
                                 'price': float(line2[2].rstrip())}
            portfolio.append(dictionary_stocks)
        return portfolio


def read_prices(filename):

    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


cost = read_portfolio('Data/portfolio.csv')
stock_prices = read_prices('Data/prices.csv')
pprint(cost)
print('***************************')
pprint(stock_prices)






