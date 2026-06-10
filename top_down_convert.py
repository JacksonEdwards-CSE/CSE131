
def get_number():
    
    return 1234

def convert_to_binary(number):
    '''Convert the passed in decimal to a binary number.
    return as a string.'''
    
    return "101101"

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
    '''Run tests to insure convert_to_binary() works correctly'''
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

    print(get_number())
    number = get_number()

    bin, oct, hex = convert(number)

    display_numbers(number, bin, oct, hex)

if __name__ == "__main__":
    main()