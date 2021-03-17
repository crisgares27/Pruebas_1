# GIVEN A LIST OF NUMBER
# IF NUMBER IS DIVISIBLE BY 3 PRINT FIZZ
# IF NUMBER IS DIVISIBLE BY 5 BUZZ
# IF NUMBER IS DIVISIBLE BY 3 AND 5 PRINT FIZZBUZZ
# if number is not divisible by 3, or 5, nor 3 and 5, print the number itself.


numbers = [2, 3, 31, 6, 9, 43, 15, 32, 30, 100, 101, 78, 99]

for number in numbers:
    if number % 3 == 0:
      if number % 5 == 0:
         print(f'FizzBuzz {number}')
      else:
         print(f'Fizz {number}')
    elif number % 5 == 0:
         print(f'Buzz {number}')
    else:
         print(f'{number}')

# Otra manera de hacerlo:

