# bounce.py
#
# Exercise 1.5

height = 100        # In meters
bounceBack = 0.6    # In meters

for i in range(1, 11):
    height = height * bounceBack
    print(i, round(height, 4))
