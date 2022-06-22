"""
 - [x] Write a short program that prints each number from 1 to 100 on a new line.
 - [x] For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
 - [x] For each multiple of 3, print "Fizz" instead of the number.
 - [x] For each multiple of 5, print "Buzz" instead of the number.
"""

# Created a for lopp that starts at 1 and ends at 100.
for number in range(1, 100):
    # prined the results of the range
    print(number)
    # if the number 3 and 5 is devided and returned by denominator that can multiply between both of them it will print Fizz Buzz.
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    # if the number is devided and returned by 3 it will print out Fizz instead of a number.
    elif number % 3 == 0:
        print('Fizz')
    # if the number is devided and returned by 5 it will print out Fizz instead of a number.
    elif number % 5 == 0:
        print('Buzz')


# Command to exit the loop and not waist extra resources.
exit()
