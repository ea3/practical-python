
import csv


def portfolio_cost(filename):
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        total = 0
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            print(record)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        return total


cost = portfolio_cost('Data/portfoliodate.csv')
print(cost)

a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2 * x for x in a if x > 6]
print(b)