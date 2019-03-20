def sum_array(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])



def fibonacci(n):
    if n < 0:
        return "The input is incorrect"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def factorial(n):
    if n < 0:
        return "No factorial for negative numbers"
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)



def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]