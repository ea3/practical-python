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

portfolio = []


def read_portfolio(filename):
    """ Computes the total cost (shares*price) of a portfolio file """

    with open(filename, 'rt') as file:
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


prices = {}


def read_prices(filename):
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

# Calculate the total cost of the portfolio
total_cost = 0

for s in portfolio:
    total_cost += s['shares'] * s['price']

print('The total cost is ', total_cost)
print('**************  ********** ***********')

# Compute the current value of the portfolio

# My answer
# portfolio_value_before = 0
# for list_from_dict in cost:
#     portfolio_value_before += int(list_from_dict['shares']) * float(list_from_dict['price'])
# print('This is the value of the portfolio before -->> ', portfolio_value_before)
# print('***** *** ** ** ** ** **')
total_value = 0.0
for s in portfolio:
    print(s)
    total_value += s['shares'] * prices[s['name']]

print('Current value ', total_value)
print('Gain', total_value - total_cost)
print('************************************************************')
print('************************************************************')


def make_report(list_of_stocks, prices_of_stocks):
    headers = ('Name', 'Price', 'Shares', 'Changes')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('    ---------- --------- --------- ---------')

    for item in portfolio:
        name_of_stock, price_of_stock, shares_of_stock, change = item['name'], item['price'], item['shares'], \
                                                                 prices[item['name']] - \
                                                                 item['price']
        print(f'{name_of_stock:>10s} {price_of_stock:>10.2f} {shares_of_stock:>10d} {change:>10.2f}')


make_report(cost, stock_prices)



#
# report = make_report(cost, prices)
# print(report)
