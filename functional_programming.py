import math

import functools

def far_to_cel(f):
    c = (f - 32) * 5/9

    return c

def map_data(map_function, data):
    mapped_data = []

    for d in data:
        mapped_data.append(map_function(d))
    
    return mapped_data

def is_prime(number):

    for n in range(2, int(math.sqrt(number)) + 1):

        if number % n == 0:
            return False
        
    return True

def main():
    # temperatures = [-43, -23, 0, 32, 85, 100, 212]

    # celcius_temperatures = map_data(far_to_cel, temperatures)

    # print(celcius_temperatures)

    # odd_values = list(filter(lambda f: f < 1000 and f and f > 0 and f % 2 == 1, list(range(0, 1000))))

    # print(odd_values)

    # divisible_by_three = list(map(lambda n: n % 3 == 0, list(range(1,100))))

    # for i in range(len(divisible_by_three) - 1):
    #     print(f'{i+1}: {divisible_by_three[i]}')

    # primes = list(filter(is_prime, range(100,201)))

    # for i in primes:
    #     print(i)

    
    # numbers = list(range(1,11))

    # sum_numbers = functools.reduce(lambda total, current : total + current , numbers)

    # print(sum_numbers)

    # factorial_numbers = functools.reduce(lambda total, current : total * current , numbers)

    # print(factorial_numbers)

    import functools
    import math

    NAME_INDEX = 0
    CATEGORY_INDEX = 1
    PRICE_INDEX = 2

    category_types = ['Clothing', 'Shoes', 'Bicycle', 'Accessories']

    shopping_list = [
        ["Bib Shorts", "Clothing", 92.50],
        ["Roubaix", "Bicycle", 3599.99],
        ["Cycling computer", "Accessories", 394.99],
        ["Helmet", "Accessories", 299.99],
        ["Road Shoes", "Shoes", 144.99],
        ["700c presta tube", "Accessories", 5.25],
        ["Jersey", "Clothing", 25.99],
        ["Multi-Function Tool", "Accessories", 22.99],
        ["Gloves", "Accessories", 8.99],
        ["Cleats", "Shoes", 15.99],
        ["Power Pedals", "Accessories", 999.99],
        ["Socks", "Clothing", 8.50]
    ]

    for category in category_types:

        category_list = list(filter(lambda shopping_item : shopping_item[CATEGORY_INDEX] == category, shopping_list))

        print(f'\n{category}')
        for i in category_list:
            print(f'\t{i}')

    trip_expenses = list(map(lambda shopping_item: shopping_item[PRICE_INDEX], shopping_list))

    trip_total = functools.reduce(lambda total, current: total + current, trip_expenses)

    print(f'{trip_total:2f}')

main()