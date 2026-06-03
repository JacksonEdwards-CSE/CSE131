
def factorial_by_loop(n):

    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

def factrorial_by_stack(n):

    if n <= 1:

        return 1

    else:
        return n * factrorial_by_stack(n - 1)

def main():

    n = 10

    total = factorial_by_loop(n)

    print(total)

    total_2 = factrorial_by_stack(n)

    print(total_2)

main()