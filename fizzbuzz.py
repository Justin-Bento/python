"""
 - [x] Write a short program that prints each number from 1 to 100 on a new line.
 - [x] For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
 - [] For each multiple of 3, print "Fizz" instead of the number.
 - [] For each multiple of 5, print "Buzz" instead of the number.
"""


for number in range(1, 100):
    print(number)
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')


exit()
