# report.py
#
# Exercise 2.4
import csv

portfolio = []


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
        header = next(file)
        total = 0
        for line in file:
            line2 = line.split(',')
            total += (int(line2[1])) * (float(line2[2]))
        return total


cost = read_portfolio('Data/portfolio.csv')
print(cost)








