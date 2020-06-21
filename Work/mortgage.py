# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000
# with Guido’s Mortgage, Stock Investment, and Bitcoin trading
# corporation.  The interest rate is 5% and the monthly payment is
# $2684.11.
#
# Here is a program that calculates the total amount that Dave will have
# to pay over the life of the mortgage:
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 60
extra_payment_end_month = 108

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if (month >= extra_payment_start_month) and (month <= extra_payment_end_month):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)

string1 = "    Here is where everything starts"
string2 = string1.strip()
print(string2)
print(string2.upper())
s = "Hello World"
t = s.replace("Hello", "replacing Hello with HALLO")
print(t)


# s = ["E", "M", "I", "L", "I", "0"]
s = "EmilioisThanos"
joinfunc = " ".join(s)
print(joinfunc)
print(s.find('T'))

string5 = b"Yo soy una frase binaria"
print(string5[0])
string6 = string5.upper()
print(string6)

decode1 = string6.decode('utf-8')
print(decode1)