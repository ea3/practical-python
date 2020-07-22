
import csv


def portfolio_cost(filename):
    with open(filename, 'rt') as file:
        header = next(file)
        total = 0
        for line in file:
            line2 = line.split(',')
            total += (int(line2[1])) * (float(line2[2]))
        return total


cost = portfolio_cost('Data/portfolio.csv')
print(cost)
