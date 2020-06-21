# pcost.py
# Exercise 1.27: Reading a data file
#
# Now that you know how to read a file, let’s write a program to perform a simple calculation.
#
# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock
# holding. Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to
# purchase all of the shares in the portfolio.
#
# Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).
#
# Your program should print output such as the following:
# Exercise 1.27


with open('Data/portfolio.csv', 'rt') as file:
    header = next(file)
    total = 0
    for line in file:
        line2 = line.split(',')
        total += (int(line2[1])) * (float(line2[2]))
    print(total)

