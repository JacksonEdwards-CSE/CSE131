# def reverse_string_recursion(string, i):

#     if i <= 0:
#         return string[i]
    
#     else:

#         return string[i] + reverse_string_recursion(string, i - 1)

# def reverse_string(string):

#     for index in range(len(string) -1, - 1, -1):

#         print(string[index], end='')

# def main():

#     string = "The quick brown fox jumps over the lazy dogs."

#     print(string)
    
#     reverse_string(string)
#     print()

#     reversed_string = reverse_string_recursion(string, len(string) - 1)

#     print(reversed_string)

def fib(n):

    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fib(n - 1) + fib(n - 2)
    
def main():

    n = 10

    number = fib(n)

    print(number)


main()