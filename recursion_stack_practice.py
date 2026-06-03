
def function_one(x):

    x += 20

    return x

def function_two(w):

    w += function_one(w)

    return w

def function_three(c):

    c += function_two(c)

    return c

def function_four(b):

    b += function_three(b)

    return b

def main():

    a = 100

    total = function_four(a)
    
    print(total)



main()