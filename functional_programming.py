
def far_to_cel(f):
    c = (f - 32) * 5/9

    return c

def map_data(map_function, data):
    mapped_data = []

    for d in data:
        mapped_data.append(map_function(d))
    
    return mapped_data

def main():
    temperatures = [-43, -23, 0, 32, 85, 100, 212]

    celcius_temperatures = map_data(far_to_cel, temperatures)

    print(celcius_temperatures)

    odd_values = list(filter(lambda f: f < 1000 and f and f > 0 and f % 2 == 1, list(range(0, 1000))))

    print(odd_values)

main()