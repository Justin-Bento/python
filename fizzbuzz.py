"""
 - [x] Write a short program that prints each number from 1 to 100 on a new line.
 - [x] For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
 - [x] For each multiple of 3, print "Fizz" instead of the number.
 - [x] For each multiple of 5, print "Buzz" instead of the number.
"""

# Return a sequence of numbers from 0 to 100.
count = range(0, 100)

# Lopp through the count's ranage.
for number in count:
    # Print FizzBuzz is both 3 and 5 are multpiles of each other.
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    # Print Fizz if the number is divided by 3.
    elif number % 3 == 0:
        print('Fizz')
    # Print Bizz if the number is divided by 5.
    elif number % 5 == 0:
        print('Buzz')

# print the results
print(number)