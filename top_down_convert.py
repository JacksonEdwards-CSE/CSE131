
def get_number():

    number = -1
    
    while number < 0:

        try:
            
            number = int(input("what is the decimal number? "))
            print()

        except ValueError:

            print("\nPlease enter a positive integer number.\n")
            
            number = -1
            

    return number

def convert_to_binary(number):

    if number == 0:
        return '0'

    binary_digits = []

    while number > 0:

        binary_digits.append(number % 2)

        number //= 2

    binary_string = ''

    for i in range(len(binary_digits)-1, -1, -1):

        binary_string += str(binary_digits[i])
    
    return binary_string

def convert_to_octal(number):
    '''Convert the passed in decimal to an octal number.
    return as a string.'''

    return "0o357"

def convert_to_hex(number):
    '''Convert the passed in decimal to a hexadecimal number.
    return as a string.'''

    return "0xEF"

def convert(number):

    '''Call functions to convert the number into 
    Binary, Octal, and Hexadecimal'''

    binary = convert_to_binary(number)

    octal = convert_to_octal(number)

    hex = convert_to_hex(number)

    return binary, octal, hex

def display_numbers(user_number, binary_number, octal_number, hex_number):

    print(f"Decimal: {user_number}, Binary: {binary_number}, Octal: {octal_number}, Hexadecimal: {hex_number}")

def test_binary():
    assert convert_to_binary(0) == '0'
    assert convert_to_binary(1) == '1'
    assert convert_to_binary(5) == '101'
    assert convert_to_binary(10) == '1010'
    assert convert_to_binary(13) == '1101'
    assert convert_to_binary(15) == '1111'
    assert convert_to_binary(16) == '10000'
    assert convert_to_binary(255) == '11111111'
    assert convert_to_binary(256) == '100000000'
    print('All Binary tests have passed.')
    return

def test_octal():
    '''Run tests to insure convert_to_octal() works correctly'''
    return

def test_hex():
    '''Run tests to insure convert_to_hex() works correctly'''
    return

def test_runner():
    '''Run all test functions'''

    test_binary()

    test_octal()

    test_hex()

    return

def main():

    test_runner()

    number = get_number()

    bin, oct, hex = convert(number)

    display_numbers(number, bin, oct, hex)

if __name__ == "__main__":
    main()