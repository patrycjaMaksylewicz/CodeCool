i = 1
next_number = 1
previous_number = 0
fib = 0
fib_length = int(input("Please write how many numbers count? "))
title = "Counting FIB"

print('Fibonacci sequance:')
while i <= fib_length:
    result = str(fib)
    print(str(i) + '. ' + result.rjust(30,' '))
    fib = next_number  + previous_number
    next_number = previous_number
    previous_number = fib
    i = i + 1

